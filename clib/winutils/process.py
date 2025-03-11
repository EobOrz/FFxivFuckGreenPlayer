import ctypes
import sys
import shlex

from .. import winapi


def iter_processes():
    hSnap = winapi.CreateToolhelp32Snapshot(0x00000002, 0)
    process_entry = winapi.ProcessEntry32()
    process_entry.dwSize = ctypes.sizeof(process_entry)
    winapi.Process32First(hSnap, ctypes.byref(process_entry))
    try:
        yield process_entry
        while 1:
            yield process_entry
            winapi.Process32Next(hSnap, ctypes.byref(process_entry))
    except WindowsError as e:
        if e.winerror != 18:
            raise
    finally:
        winapi.CloseHandle(hSnap)


def pid_by_executable(executable_name: bytes | str):
    if isinstance(executable_name, str):
        executable_name = executable_name.encode(winapi.DEFAULT_ENCODING)
    for process in iter_processes():
        if process.szExeFile == executable_name:
            yield process.th32ProcessID


def run_admin():
    try:
        if ctypes.windll.shell32.IsUserAnAdmin(): return
    except:
        pass
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    raise PermissionError("Need admin permission, a new process should be started, if not, please run it as admin manually")


def enable_privilege():
    hProcess = ctypes.c_void_p(winapi.GetCurrentProcess())
    if winapi.OpenProcessToken(hProcess, 32, ctypes.byref(hProcess)):
        tkp = winapi.TOKEN_PRIVILEGES()
        winapi.LookupPrivilegeValue(None, "SeDebugPrivilege", ctypes.byref(tkp.Privileges[0].Luid))
        tkp.count = 1
        tkp.Privileges[0].Attributes = 2
        winapi.AdjustTokenPrivileges(hProcess, 0, ctypes.byref(tkp), 0, None, None)


class create_suspend_process:
    def __init__(self, cmd, **kwargs):
        if isinstance(cmd, (list, tuple)):
            cmd = shlex.join(cmd)
        if isinstance(cmd, str):
            cmd = cmd.encode(winapi.DEFAULT_ENCODING)
        assert isinstance(cmd, bytes), type(cmd)
        self.cmd = cmd
        self.process_information = None
        self.startup_info = winapi.STARTUPINFOA(**kwargs)

    def start(self):
        assert not self.process_information, "Process already started"
        self.process_information = winapi.PROCESS_INFORMATION()
        winapi.CreateProcessA(
            None, self.cmd,
            None, None, 0,
            4 | 8,  # CREATE_SUSPENDED | DETACHED_PROCESS
            None, None,
            ctypes.byref(self.startup_info), ctypes.byref(self.process_information)
        )
        return self

    def resume(self):
        assert self.process_information, "Process not started"
        winapi.ResumeThread(self.process_information.hThread)

    def wait(self):
        assert self.process_information, "Process not started"
        winapi.WaitForSingleObject(self.process_information.hProcess, -1)

    def __del__(self):
        if self.process_information:
            winapi.CloseHandle(self.process_information.hProcess)
            winapi.CloseHandle(self.process_information.hThread)

    def __enter__(self):
        return self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # self.wait()
        self.resume()
