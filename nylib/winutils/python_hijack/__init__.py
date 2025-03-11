import configparser
import os
import pathlib
import shutil
import subprocess
import sys
import sysconfig
import tempfile

DLLMAIN_TEMPLATE = '''
'''


def iter_pe_exported(pe_path):
    from ...utils.pip import required
    required('pefile')
    import pefile
    pe = pefile.PE(pe_path)
    for exp in pe.DIRECTORY_ENTRY_EXPORT.symbols:
        yield exp.name.decode('utf-8'), exp.address, exp.ordinal
    pe.close()


def create_src(pe_path, dst_dir, default_config):
    names = [(name, ordinal) for name, _, ordinal in iter_pe_exported(pe_path)]
    dst = pathlib.Path(dst_dir)
    shutil.rmtree(dst, ignore_errors=True)
    dst.mkdir(parents=True, exist_ok=True)

    addr_var = lambda n: '_pyhijack_val_' + n
    func_asm = lambda n: '_pyhijack_func_' + n

    current_dir = pathlib.Path(sys.executable if getattr(sys, "frozen", False) else __file__).parent
    if (dllmain_template_path := current_dir / 'dllmain.template.cpp').exists():
        dllmain_text = dllmain_template_path.read_text('utf-8')
    else:
        dllmain_text = DLLMAIN_TEMPLATE
    dllmain_text = dllmain_text.replace("/*REPLACE_ORIG_DLL_HERE*/", default_config['orig'].replace('\\', '\\\\'))
    dllmain_text = dllmain_text.replace("/*REPLACE_PY_DLL_HERE*/", default_config['python_dll'].replace('\\', '\\\\'))
    dllmain_text = dllmain_text.replace("/*REPLACE_PY_MAIN_HERE*/", default_config['python_main'].replace('\\', '\\\\'))

    buf = ''
    for name, ordinal in names:
        buf += f'#pragma comment(linker, "/EXPORT:{name}={func_asm(name)},@{ordinal}")\n'
    buf += '\nextern "C" {\n'
    for name, ordinal in names:
        buf += f'    PVOID {addr_var(name)};\n'
    buf += '}\n'
    dllmain_text = dllmain_text.replace("/*REPLACE_DEF_EXPORT_HERE*/", buf)

    buf = ''
    for name, ordinal in names:
        buf += (f'    {addr_var(name)} = (PVOID)GetProcAddress(hOrig, "{name}");\n'
                f'    if ({addr_var(name)} == NULL) {{\n'
                f'       HANDLE_ERROR(L"GetProcAddress({name}) failed: %d", GetLastError());\n'
                f'    }}\n')

    dllmain_text = dllmain_text.replace("/*REPLACE_SET_EXPORT_HERE*/", buf)

    (dst / 'dllmain.cpp').write_text(dllmain_text, 'utf-8')

    dllasm_text = '.Data\n'
    for name, ordinal in names:
        dllasm_text += f'EXTERN {addr_var(name)}:dq;\n'
    dllasm_text += '\n.Code\n'
    for name, ordinal in names:
        dllasm_text += (f'{func_asm(name)} PROC\n'
                        f'    jmp {addr_var(name)}\n'
                        f'{func_asm(name)} ENDP\n\n')
    dllasm_text += '\nEND\n'
    (dst / 'dllasm.asm').write_text(dllasm_text, 'utf-8')


def hijack(pe_path, build_dir=None, default_config=None, dst_dir=None):
    from .. import msvc, ensure_env
    from ...process import Process

    ensure_env.ensure_msvc()

    need_move_orig = False
    orig_path = pe_path = pathlib.Path(pe_path).absolute()
    dst_dir = pathlib.Path(dst_dir) if dst_dir is not None else pe_path.parent
    dst_path = dst_dir / pe_path.name
    if dst_path == orig_path:
        need_move_orig = True
        orig_path = orig_path.with_suffix('.pyHijack' + orig_path.suffix)

    plat_spec = 'x86_amd64'  # TODO: check
    build_env = msvc.load_vcvarsall(plat_spec)

    py_dll = f"python{sys.version_info.major}{sys.version_info.minor}.dll"
    if default_config is None:
        default_config = {}
    default_config = {
                         'orig': str(orig_path),
                         'create_console': '1',  # empty string to hide console
                         'python_dll': Process.current.get_ldr_data(py_dll).FullDllName.value,
                         'python_main': '.\\main.py',
                     } | default_config

    if build_dir is None:
        tmp_dir = tempfile.mkdtemp()
    else:
        tmp_dir = build_dir
    try:
        tmp_dir = pathlib.Path(tmp_dir)
        create_src(pe_path, tmp_dir, default_config)
        ml = msvc.where('ml64.exe', plat_spec)
        cl = msvc.where('cl.exe', plat_spec)
        include_path = sysconfig.get_paths()['include']
        libs_path = str(pathlib.Path(include_path).with_name('libs'))
        subprocess.run([ml, '/c', '/Fo', tmp_dir / 'dllasm.obj', tmp_dir / 'dllasm.asm'], cwd=tmp_dir, env=build_env, check=True, shell=True)
        subprocess.run([
            cl,
            '/D_USRDLL', '/D_WINDLL',
            # '/I', sysconfig.get_paths()['include'], f'/LIBPATH:"{libs_path}"',
            tmp_dir / 'dllmain.cpp', tmp_dir / 'dllasm.obj',
            '/link', '/DLL', '/OUT:' + str(tmp_dir / 'hijacked.dll')
        ], cwd=tmp_dir, env=build_env, check=True, shell=True)
        if need_move_orig:
            pe_path.rename(orig_path)
        # (tmp_dir / 'hijacked.dll').rename(dst_path)
        with open(dst_path, 'wb') as f:
            f.write((tmp_dir / 'hijacked.dll').read_bytes())
    finally:
        if build_dir is None:
            shutil.rmtree(tmp_dir, ignore_errors=True)

    cgh_path = dst_path.with_name('pyHijack.ini')
    config = configparser.ConfigParser()
    config['Hijack'] = default_config
    config['Python'] = {
        'path': os.pathsep.join(sys.path),
    }
    with open(cgh_path, 'w') as f:
        config.write(f)
