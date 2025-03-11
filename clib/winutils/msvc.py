import contextlib
import functools
import itertools
import os
import os.path
import subprocess
import winreg


@functools.cache
def msvc14_find_vc2017():
    if not (root := os.environ.get("ProgramFiles(x86)") or os.environ.get("ProgramFiles")): return None, None

    for component in (
            "Microsoft.VisualStudio.Component.VC.Tools.x86.x64",
            "Microsoft.VisualStudio.Workload.WDExpress",
    ):
        with contextlib.suppress(subprocess.CalledProcessError, OSError, UnicodeDecodeError):
            path = subprocess.check_output([
                os.path.join(root, "Microsoft Visual Studio", "Installer", "vswhere.exe"),
                "-latest", "-prerelease", "-requires", component, "-property", "installationPath", "-products", "*",
            ]).decode(encoding="mbcs", errors="strict").strip()
            path = os.path.join(path, "VC", "Auxiliary", "Build")
            if os.path.isdir(path): return 15, path

    path = os.path.join(os.getenv('SystemDrive'), 'BuildTools', 'VC', 'Auxiliary', 'Build')  # default path for BuildTools
    if os.path.isdir(path): return 15, path
    return None, None


@functools.cache
def msvc14_find_vc2015():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\VisualStudio\SxS\VC7", 0, winreg.KEY_READ | winreg.KEY_WOW64_32KEY, )
    except OSError:
        return None, None
    best_version = 0
    best_dir = None
    with key:
        for i in itertools.count():
            try:
                v, vc_dir, vt = winreg.EnumValue(key, i)
            except OSError:
                break
            if v and vt == winreg.REG_SZ and os.path.isdir(vc_dir):
                try:
                    version = int(float(v))
                except (ValueError, TypeError):
                    continue
                if version >= 14 and version > best_version:
                    best_version, best_dir = version, vc_dir
    return best_version, best_dir


@functools.cache
def msvc14_find_vcvarsall(plat_spec):
    vcruntime = None
    vcruntime_plat = {
        'x86': 'x86',
        'x86_amd64': 'x64',
        'x86_arm': 'arm',
        'x86_arm64': 'arm64',
    }.get(plat_spec, 'x64' if 'amd64' in plat_spec else 'x86')
    _, best_dir = msvc14_find_vc2017()
    if best_dir:
        vcredist = os.path.join(best_dir, "..", "..", "redist", "MSVC", "**", vcruntime_plat, "Microsoft.VC14*.CRT", "vcruntime140.dll", )
        vcredist = os.path.normpath(vcredist)
        try:
            import glob

            vcruntime = glob.glob(vcredist, recursive=True)[-1]
        except (ImportError, OSError, LookupError):
            vcruntime = None
    else:
        best_version, best_dir = msvc14_find_vc2015()
        if best_version:
            vcruntime = os.path.join(best_dir, 'redist', vcruntime_plat, "Microsoft.VC140.CRT", "vcruntime140.dll", )
    if not best_dir:
        return None, None
    vcvarsall = os.path.join(best_dir, "vcvarsall.bat")
    if not os.path.isfile(vcvarsall): return None, None
    if not vcruntime or not os.path.isfile(vcruntime): vcruntime = None
    return vcvarsall, vcruntime


@functools.cache
def load_vcvarsall(plat_spec):
    vcvarsall, _ = msvc14_find_vcvarsall(plat_spec)
    if not vcvarsall:
        raise FileNotFoundError("vcvarsall.bat not found")
    try:
        out = subprocess.check_output(f'cmd /u /c "{vcvarsall}" {plat_spec} && set').decode('utf-16le', errors='replace')
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(f"Error executing {exc.cmd}") from exc
    return {
        key: value
        for key, _, value in (line.partition('=') for line in out.splitlines())
        if key and value
    }


def where(exe, plat_spec):
    paths = load_vcvarsall(plat_spec).get("Path", "").split(os.pathsep)
    for path in paths:
        if os.path.exists(exe_path := os.path.join(os.path.abspath(path), exe)):
            return exe_path
    raise FileNotFoundError(f"{exe} not found in PATH")
