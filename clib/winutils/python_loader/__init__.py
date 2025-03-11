import ctypes
import os
import pathlib
import shutil
import subprocess
import sys
import tempfile
import time

from ...process import Process


def build_loader(dst, build_dir=None):
    from .. import msvc, ensure_env
    ensure_env.ensure_msvc()
    plat_spec = 'x86_amd64'  # TODO: check
    build_env = msvc.load_vcvarsall(plat_spec)
    dst = pathlib.Path(dst).absolute()
    assert not dst.exists(), f"File already exists: {dst}"
    if build_dir is None:
        tmp_dir = pathlib.Path(tempfile.mkdtemp())
    else:
        tmp_dir = pathlib.Path(build_dir)
        tmp_dir.mkdir(exist_ok=True, parents=True)
    src_file = pathlib.Path(__file__).parent / 'python_loader.cpp'
    try:
        subprocess.run([
            msvc.where('cl.exe', plat_spec),
            '/D_WINDLL', '/std:c++20', '/EHsc',  # '/DEBUG', '/Zi',
            src_file,
            '/link', '/DLL', '/OUT:' + str(dst),
        ], cwd=tmp_dir, env=build_env, check=True, shell=True)
    finally:
        if build_dir is None:
            shutil.rmtree(tmp_dir, ignore_errors=True)
    for file in dst.with_suffix('.exp'), dst.with_suffix('.obj'), dst.with_suffix('.lib'):
        if file.exists():
            file.unlink()


def run_script(process: Process, main_script, python_dll=None, python_paths=None, loader=None):
    if loader is None:
        loader = pathlib.Path(__file__).parent / 'python_loader.dll'
    if not loader.exists():
        build_loader(loader)

    loader = process.load_library(loader)
    pLoadPython = process.get_proc_address(loader, "LoadPython")

    if python_dll is None:
        dll_name = f"python{sys.version_info.major}{sys.version_info.minor}.dll"
        python_dll = Process.current.get_ldr_data(dll_name).FullDllName.value
    else:
        python_dll = os.path.abspath(python_dll)
    if python_paths is None:
        python_paths = os.pathsep.join(sys.path)
    main_script = os.path.abspath(main_script)

    ws_pyDll = python_dll.encode('utf-16-le') + b'\0\0'
    ws_pyMain = main_script.encode('utf-16-le') + b'\0\0'
    ws_pyPaths = python_paths.encode('utf-16-le') + b'\0\0'

    p_config = process.alloc(3 * 8 + len(ws_pyDll) + len(ws_pyMain) + len(ws_pyPaths))
    process.write_ptr(p_config, p_config + 3 * 8)
    process.write_ptr(p_config + 8, p_config + 3 * 8 + len(ws_pyDll))
    process.write_ptr(p_config + 16, p_config + 3 * 8 + len(ws_pyDll) + len(ws_pyMain))
    process.write(p_config + 24, ws_pyDll)
    process.write(p_config + 24 + len(ws_pyDll), ws_pyMain)
    process.write(p_config + 24 + len(ws_pyDll) + len(ws_pyMain), ws_pyPaths)
    process.call(pLoadPython, p_config)
