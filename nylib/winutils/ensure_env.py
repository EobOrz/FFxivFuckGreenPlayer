import atexit
import ctypes
import itertools
import logging
import os
import os.path
import pathlib
import shlex
import shutil
import subprocess
import tarfile
import tempfile
import time
import winreg

from . import msvc
from ..utils.web import download

logger = logging.getLogger(__name__)


def get_tmpdir():
    if hasattr(get_tmpdir, 'path'): return get_tmpdir.path
    get_tmpdir.path = tempfile.mkdtemp()
    atexit.register(shutil.rmtree, get_tmpdir.path, ignore_errors=True)
    return get_tmpdir.path


def get_sys_env(name):
    return winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager\Environment", 0, winreg.KEY_READ), name)[0]


def set_sys_env(name, value):
    winreg.SetValueEx(winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"System\CurrentControlSet\Control\Session Manager\Environment", 0, winreg.KEY_SET_VALUE), name, 0, winreg.REG_EXPAND_SZ, value)


def get_user_env(name):
    return winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment"), name)[0]


def set_user_env(name, value):
    winreg.SetValueEx(winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"Environment"), name, 0, winreg.REG_EXPAND_SZ, value)


def reload_env_path():
    time.sleep(1)  # wait for the environment to update
    sys_path = get_sys_env('Path')
    user_path = get_user_env('Path')
    old_env = os.environ['Path'].split(os.pathsep)
    for p in itertools.chain(sys_path.split(os.pathsep), user_path.split(os.pathsep)):
        if not p: continue
        p = os.path.expandvars(p)
        if p not in old_env:
            old_env.append(p)
    os.environ['Path'] = os.pathsep.join(old_env)
    return os.environ['Path']


def find_by_uninstall(name):
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall",
        0, winreg.KEY_READ
    )
    try:
        i = 0
        while True:
            try:
                subkey = winreg.OpenKey(key, winreg.EnumKey(key, i))
                try:
                    display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                    if name in display_name:
                        return winreg.QueryValueEx(subkey, "InstallLocation")[0]
                except FileNotFoundError:
                    pass
                finally:
                    winreg.CloseKey(subkey)
            except OSError:
                break
            finally:
                i += 1
    finally:
        winreg.CloseKey(key)


def ensure_winget(tmp_dir=None, shell=True):
    if p := shutil.which('winget'): return p
    tmp_dir = pathlib.Path(tmp_dir or get_tmpdir())

    download('https://aka.ms/getwinget', tmp_dir / 'Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle', show_progress=shell)
    download('https://aka.ms/Microsoft.VCLibs.x64.14.00.Desktop.appx', tmp_dir / 'Microsoft.VCLibs.x64.14.00.Desktop.appx', show_progress=shell)
    download('https://github.com/microsoft/microsoft-ui-xaml/releases/download/v2.8.6/Microsoft.UI.Xaml.2.8.x64.appx', tmp_dir / 'Microsoft.UI.Xaml.2.8.x64.appx', show_progress=shell)
    subprocess.check_call(["powershell", "-Command", "Add-AppxPackage", tmp_dir / 'Microsoft.VCLibs.x64.14.00.Desktop.appx'], shell=shell)
    subprocess.check_call(["powershell", "-Command", "Add-AppxPackage", tmp_dir / 'Microsoft.UI.Xaml.2.8.x64.appx'], shell=shell)
    subprocess.check_call(["powershell", "-Command", "Add-AppxPackage", tmp_dir / 'Microsoft.DesktopAppInstaller_8wekyb3d8bbwe.msixbundle'], shell=shell)

    if p := shutil.which('winget'): return p
    raise FileNotFoundError('winget not found')


def ensure_git(shell=True):
    if p := shutil.which('git'): return p
    winget = ensure_winget(shell=shell)
    subprocess.check_call([winget, 'install', '--id', 'Git.Git', '-e', '--source', 'winget'], shell=shell)

    reload_env_path()
    if p := shutil.which('git'): return p
    raise FileNotFoundError('git not found')


def ensure_cmake(tmp_dir=None, shell=True):
    if p := shutil.which('cmake'): return p
    tmp_dir = pathlib.Path(tmp_dir or get_tmpdir())

    download(
        r'https://github.com/Kitware/CMake/releases/download/v3.29.3/cmake-3.29.3-windows-x86_64.msi',
        tmp_dir / 'cmake-3.29.3-windows-x86_64.msi',
        show_progress=shell
    )

    subprocess.check_call([
        "msiexec", "/i", tmp_dir / 'cmake-3.29.3-windows-x86_64.msi', "/passive", "/norestart"
    ], shell=shell)

    # msi installer does not update the path if call in passive mode
    pg_files = os.environ.get("ProgramFiles") or os.environ.get("ProgramFiles(x86)")
    if not pg_files: raise FileNotFoundError('ProgramFiles not found')
    cmake_dir = pathlib.Path(pg_files) / 'CMake' / 'bin'
    if not cmake_dir.exists(): raise FileNotFoundError('cmmake not found')
    if ctypes.windll.shell32.IsUserAnAdmin():
        set_sys_env('Path', f'{get_sys_env("Path")};{cmake_dir}')
    else:
        set_user_env('Path', f'{get_user_env("Path")};{cmake_dir}')
    reload_env_path()
    if p := shutil.which('cmake'): return p
    raise FileNotFoundError('cmake not found')


def ensure_msvc(tmp_dir=None, shell=True):
    # https://aka.ms/vs/17/release/vs_buildtools.exe
    # vs_buildtools.exe --quiet --wait --norestart --installPath C:\BuildTools --add Microsoft.VisualStudio.Workload.VCTools --add Microsoft.VisualStudio.Component.Windows10SDK
    _, p = msvc.msvc14_find_vc2017()
    if p: return p

    tmp_dir = pathlib.Path(tmp_dir or get_tmpdir())

    download('https://aka.ms/vs/17/release/vs_buildtools.exe', tmp_dir / 'vs_buildtools.exe', show_progress=shell)
    subprocess.check_call([
        tmp_dir / 'vs_buildtools.exe',
        '--wait', '--norestart', '--passive',
        '--add', 'Microsoft.VisualStudio.Workload.VCTools',
        '--add', 'Microsoft.VisualStudio.Component.Windows10SDK.19041',
        '--add', 'Microsoft.VisualStudio.Component.Windows11SDK.22000',
        '--add', 'Microsoft.VisualStudio.Component.VC.CMake.Project',
    ], shell=shell)

    msvc.msvc14_find_vc2017.cache_clear()
    reload_env_path()
    _, p = msvc.msvc14_find_vc2017()
    if p: return p
    raise FileNotFoundError('msvc not found')


def _find_cygwin_dir():
    try:
        reg = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Cygwin\setup", 0, winreg.KEY_READ)
        path, _ = winreg.QueryValueEx(reg, 'rootdir')
    except FileNotFoundError:
        return None
    else:
        path = pathlib.Path(path) / 'bin'
        if (path / 'cygcheck.exe').is_file(): return path


def ensure_cygwin_dir(tmp_dir=None, shell=True):
    # https://www.cygwin.com/setup-x86_64.exe
    # at SOFTWARE\Cygwin\setup
    if path := _find_cygwin_dir(): return path

    tmp_dir = pathlib.Path(tmp_dir or get_tmpdir())

    download('https://www.cygwin.com/setup-x86_64.exe', tmp_dir / 'cygwin-setup-x86_64.exe', show_progress=shell)
    p = pathlib.Path(f'{os.getenv("SystemDrive")}\\MyBuildTools\\cygwin64')
    assert not p.exists()
    install_root = p / 'Cygwin64'
    local_root = p / 'local'
    local_root.mkdir(parents=True, exist_ok=True)

    subprocess.check_call([
        tmp_dir / 'cygwin-setup-x86_64.exe',
        '--quiet-mode', '--wait',
        # allow user input?
        '--root', install_root,
        '--local-package-dir', local_root,
        '--site', 'http://mirrors.kernel.org/sourceware/cygwin/',
    ], shell=shell)

    if path := _find_cygwin_dir(): return path
    raise FileNotFoundError('cygwin not found')


def _find_msys2_dir():
    return find_by_uninstall('MSYS2')


def ensure_msys2(tmp_dir=None, shell=True):
    if p := _find_msys2_dir(): return p

    tmp_dir = pathlib.Path(tmp_dir or get_tmpdir())
    download(
        r'https://github.com/msys2/msys2-installer/releases/download/2024-05-07/msys2-x86_64-20240507.exe',
        tmp_dir / 'msys2-x86_64-20240507.exe', show_progress=shell
    )
    p = pathlib.Path(f'{os.getenv("SystemDrive")}\\MyBuildTools\\msys2')
    # msys2-x86_64-20240507.exe -t "C:\path\to\installation\location" --al --am --da -c
    subprocess.check_call([
        tmp_dir / 'msys2-x86_64-20240507.exe',
        '--al', '--da', '-c', 'install', '-t', p,
    ], shell=shell)

    if p := _find_msys2_dir(): return p
    raise FileNotFoundError('msys2 not found')


def make_msys2_shell(args):
    p = _find_msys2_dir()
    if not p: raise FileNotFoundError('msys2 not found')
    return [pathlib.Path(p) / 'msys2_shell.cmd', '-defterm', '-no-start', '-c', shlex.join(map(str, args))]


def ensure_msys2_file(fp, shell=True):
    if not hasattr(ensure_msys2_file, 'cache'):
        ensure_msys2_file.cache = {}
    elif fp in ensure_msys2_file.cache:
        return ensure_msys2_file.cache[fp]
    fp_ = os.path.join(_find_msys2_dir(), fp.lstrip('/\\'))
    if not os.path.exists(fp_):
        ensure_msys2()
        if not hasattr(ensure_msys2_file, 'db_loaded'):
            subprocess.check_output(make_msys2_shell(['pacman', '-Fy']), shell=shell)
            ensure_msys2_file.db_loaded = True
        package_ = subprocess.check_output(make_msys2_shell(['pacman', '-F', '-q', fp]))
        mode, package = package_.split()[0].decode('utf-8').split('/', 1)
        ensure_msys2_package(package, shell=shell)
    ensure_msys2_file.cache[fp] = fp_
    return fp_


def ensure_msys2_package(pkg, shell=True):
    if not hasattr(ensure_msys2_package, 'cache'):
        ensure_msys2_package.cache = {}
    elif pkg in ensure_msys2_package.cache:
        return
    ensure_msys2()
    try:
        subprocess.check_output(make_msys2_shell(['pacman', '-Q', pkg]), shell=shell)
    except subprocess.CalledProcessError:
        pass
    else:
        ensure_msys2_package.cache[pkg] = True
        return
    subprocess.check_output(make_msys2_shell(['pacman', '-S', '--noconfirm', '--needed', pkg]), shell=shell)
    ensure_msys2_package.cache[pkg] = True
