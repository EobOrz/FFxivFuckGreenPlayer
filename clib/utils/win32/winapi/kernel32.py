import ctypes
from ctypes import wintypes

from . import structure

dll = ctypes.WinDLL('kernel32.dll')
#: Opens an existing local process object.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684320%28v=vs.85%29.aspx
OpenProcess = dll.OpenProcess
OpenProcess.restype = wintypes.HANDLE
OpenProcess.argtypes = [
    wintypes.DWORD,
    wintypes.BOOL,
    wintypes.DWORD,
]
#: Terminates the specified process and all of its threads.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms686714%28v=vs.85%29.aspx
TerminateProcess = dll.TerminateProcess
TerminateProcess.restype = wintypes.BOOL
TerminateProcess.argtypes = [
    wintypes.HANDLE,
    wintypes.UINT,
]

#: Closes an open object handle.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms724211%28v=vs.85%29.aspx
CloseHandle = dll.CloseHandle
CloseHandle.restype = wintypes.BOOL
CloseHandle.argtypes = [
    wintypes.HANDLE
]

#: Retrieves the calling thread's last-error code value. The last-error code is maintained on a per-thread basis.
#: Multiple threads do not overwrite each other's last-error code.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms679360%28v=vs.85%29.aspx
GetLastError = dll.GetLastError
GetLastError.restype = wintypes.DWORD

#: Retrieves a pseudo handle for the current process.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms683179%28v=vs.85%29.aspx
GetCurrentProcess = dll.GetCurrentProcess
GetCurrentProcess.restype = wintypes.HANDLE

#: Reads data from an area of memory in a specified process. The entire area to be read must be accessible or the operation fails.
#:
#: https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-readprocessmemory
ReadProcessMemory = dll.ReadProcessMemory
ReadProcessMemory.argtypes = (
    wintypes.HANDLE,
    wintypes.LPCVOID,
    wintypes.LPVOID,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
)
ReadProcessMemory.restype = wintypes.BOOL

#: Writes data to an area of memory in a specified process.
#: The entire area to be written to must be accessible or the operation fails.
#:
#: https://learn.microsoft.com/en-us/windows/win32/api/memoryapi/nf-memoryapi-writeprocessmemory
WriteProcessMemory = dll.WriteProcessMemory
WriteProcessMemory.argtypes = [
    wintypes.HANDLE,
    wintypes.LPCVOID,
    wintypes.LPVOID,
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)
]
WriteProcessMemory.restype = wintypes.BOOL

#: Enables a debugger to attach to an active process and debug it.
#:
#: https://learn.microsoft.com/en-us/windows/win32/api/debugapi/nf-debugapi-debugactiveprocess
DebugActiveProcess = dll.DebugActiveProcess
DebugActiveProcess.restype = wintypes.BOOL
DebugActiveProcess.argtypes = [
    wintypes.DWORD,
]

#: Reserves or commits a region of memory within the virtual address space of a specified process.
#: The function initializes the memory it allocates to zero, unless MEM_RESET is used.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366890%28v=vs.85%29.aspx
VirtualAllocEx = dll.VirtualAllocEx
VirtualAllocEx.restype = wintypes.LPVOID
VirtualAllocEx.argtypes = (
    wintypes.HANDLE,
    wintypes.LPVOID,
    ctypes.c_size_t,
    wintypes.DWORD,
    wintypes.DWORD
)

#: Changes the protection on a region of committed pages in the virtual address space of a specified process.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366899%28v=vs.85%29.aspx
VirtualProtectEx = dll.VirtualProtectEx
VirtualProtectEx.restype = ctypes.c_long
VirtualProtectEx.argtypes = (
    ctypes.c_void_p,
    ctypes.c_void_p,
    ctypes.c_size_t,
    ctypes.c_ulong,
    ctypes.POINTER(ctypes.c_ulong)
)

#: Takes a snapshot of the specified processes, as well as the heaps, modules, and threads used by these processes.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms682489%28v=vs.85%29.aspx
CreateToolhelp32Snapshot = dll.CreateToolhelp32Snapshot
CreateToolhelp32Snapshot.restype = ctypes.c_void_p
CreateToolhelp32Snapshot.argtypes = (ctypes.c_ulong, ctypes.c_ulong)

#: Retrieves information about the first module associated with a process.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684218%28v=vs.85%29.aspx
Module32First = dll.Module32First
Module32First.restype = ctypes.c_ulonglong
Module32First.argtypes = (ctypes.c_void_p, structure.LPMODULEENTRY32)

#: Retrieves information about the next module associated with a process or thread.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684221%28v=vs.85%29.aspx
Module32Next = dll.Module32Next
Module32Next.restype = ctypes.c_ulonglong
Module32Next.argtypes = (ctypes.c_void_p, structure.LPMODULEENTRY32)

#: Retrieves information about the first process encountered in a system snapshot.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684834%28v=vs.85%29.aspx
Process32First = dll.Process32First
Process32First.restype = ctypes.c_long

#: Retrieves information about the next process recorded in a system snapshot.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684836%28v=vs.85%29.aspx
Process32Next = dll.Process32Next
Process32Next.restype = ctypes.c_long

#: Retrieves information about the first thread of any process encountered in a system snapshot.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms686728%28v=vs.85%29.aspx
Thread32First = dll.Thread32First
Thread32First.restype = ctypes.c_long
Thread32First.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(structure.ThreadEntry32)
]

#: Retrieves information about the next thread of any process encountered in the system memory snapshot.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms686731%28v=vs.85%29.aspx
Thread32Next = dll.Thread32Next
Thread32Next.restype = ctypes.c_long
Thread32Next.argtypes = [
    ctypes.c_void_p,
    ctypes.POINTER(structure.ThreadEntry32)
]

#: Opens an existing thread object.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684335%28v=vs.85%29.aspx
OpenThread = dll.OpenThread
OpenThread.restype = ctypes.c_void_p
OpenThread.argtypes = [
    ctypes.c_ulong,
    ctypes.c_long,
    ctypes.c_ulong
]

#: Suspends the specified thread.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms686345%28v=vs.85%29.aspx
SuspendThread = dll.SuspendThread
SuspendThread.restype = ctypes.c_ulong

#: Decrements a thread's suspend count. When the suspend count is decremented to zero, the execution of the thread is resumed.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms685086%28v=vs.85%29.aspx
ResumeThread = dll.ResumeThread
ResumeThread.restype = ctypes.c_ulong
ResumeThread.argtypes = [ctypes.c_void_p]

#: Retrieves the context of the specified thread.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms679362%28v=vs.85%29.aspx
GetThreadContext = dll.GetThreadContext
GetThreadContext.restype = ctypes.c_long

#: Sets the context for the specified thread.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms680632%28v=vs.85%29.aspx
SetThreadContext = dll.SetThreadContext
SetThreadContext.restype = ctypes.c_long

#: Releases, decommits, or releases and decommits a region of memory within the virtual address space of a specified process.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366894%28v=vs.85%29.aspx
VirtualFreeEx = dll.VirtualFreeEx
VirtualFreeEx.restype = ctypes.c_long

#: Retrieves information about a range of pages in the virtual address space of the calling process.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/aa366907(v=vs.85).aspx
VirtualQueryEx = dll.VirtualQueryEx
VirtualQueryEx.argtypes = [ctypes.wintypes.HANDLE, ctypes.wintypes.LPCVOID, ctypes.c_void_p, ctypes.c_size_t]
VirtualQueryEx.restype = ctypes.c_ulong

#: Determines whether the specified process is running under WOW64.
#:
#: https://msdn.microsoft.com/en-us/library/ms684139(v=vs.85).aspx
IsWow64Process = dll.IsWow64Process
IsWow64Process.restype = ctypes.c_long

#: Retrieves information about the current system.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms724381(v=vs.85).aspx
GetSystemInfo = dll.GetSystemInfo
GetSystemInfo.restype = ctypes.c_void_p

GetModuleHandleW = dll.GetModuleHandleW
GetModuleHandleW.restype = ctypes.c_void_p
GetModuleHandleW.argtypes = [ctypes.c_wchar_p]

GetModuleHandleA = dll.GetModuleHandleA
GetModuleHandleA.restype = ctypes.c_void_p
GetModuleHandleA.argtypes = [ctypes.c_wchar_p]

GetProcAddress = dll.GetProcAddress
GetProcAddress.restype = ctypes.c_void_p
GetProcAddress.argtypes = (
    ctypes.c_void_p,  # hModule
    ctypes.c_char_p,  # lpProcName
)

CreateRemoteThread = dll.CreateRemoteThread
CreateRemoteThread.restype = ctypes.c_void_p
CreateRemoteThread.argtypes = (
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # lpThreadAttributes
    ctypes.c_size_t,  # dwStackSize
    ctypes.c_void_p,  # lpStartAddress
    ctypes.c_void_p,  # lpParameter
    ctypes.c_ulong,  # dwCreationFlags
    ctypes.c_void_p,  # lpThreadId
)

GetFullPathNameA = dll.GetFullPathNameA
GetFullPathNameA.restype = ctypes.c_ulong
GetFullPathNameA.argtypes = [
    ctypes.c_char_p,  # lpFileName
    ctypes.c_ulong,  # nBufferLength
    ctypes.c_char_p,  # lpBuffer
    ctypes.POINTER(ctypes.c_char_p),  # lpFilePart
]

WaitForSingleObject = dll.WaitForSingleObject
WaitForSingleObject.restype = ctypes.c_ulong
WaitForSingleObject.argtypes = [
    ctypes.c_void_p,  # hHandle
    ctypes.c_ulong,  # dwMilliseconds
]

GetExitCodeThread = dll.GetExitCodeThread
GetExitCodeThread.restype = ctypes.c_long
GetExitCodeThread.argtypes = [
    ctypes.c_void_p,  # hThread
    ctypes.POINTER(ctypes.c_ulong),  # lpExitCode
]

VirtualFreeEx = dll.VirtualFreeEx
VirtualFreeEx.restype = ctypes.c_long
VirtualFreeEx.argtypes = [
    ctypes.c_void_p,  # hProcess
    ctypes.c_void_p,  # lpAddress
    ctypes.c_size_t,  # dwSize
    ctypes.c_ulong,  # dwFreeType
]

GetThreadTimes = dll.GetThreadTimes
GetThreadTimes.restype = ctypes.c_long
GetThreadTimes.artypes = [
    ctypes.c_void_p,  # hThread
    ctypes.POINTER(structure.FILETIME),  # lpCreationTime
    ctypes.POINTER(structure.FILETIME),  # lpExitTime
    ctypes.POINTER(structure.FILETIME),  # lpKernelTime
    ctypes.POINTER(structure.FILETIME),  # lpUserTime
]

GetModuleFileName = dll.GetModuleFileNameA
GetModuleFileName.restype = ctypes.c_ulong
GetModuleFileName.argtypes = [
    ctypes.c_void_p,  # hModule
    ctypes.c_void_p,  # lpFilename
    ctypes.c_ulong,  # nSize
]

DuplicateHandle = dll.DuplicateHandle
DuplicateHandle.restype = ctypes.c_bool
DuplicateHandle.argtypes = [
    ctypes.c_void_p,  # hSourceProcessHandle
    ctypes.c_void_p,  # hSourceHandle
    ctypes.c_void_p,  # hTargetProcessHandle
    ctypes.POINTER(ctypes.c_void_p),  # lpTargetHandle
    ctypes.c_ulong,  # dwDesiredAccess
    ctypes.c_bool,  # bInheritHandle
    ctypes.c_ulong  # dwOptions
]

CreateFileA = dll.CreateFileA
CreateFileA.restype = structure.c_address
CreateFileA.argtypes = [
    ctypes.c_char_p,  # lpFileName
    ctypes.c_ulong,  # dwDesiredAccess
    ctypes.c_ulong,  # dwShareMode
    ctypes.c_void_p,  # lpSecurityAttributes
    ctypes.c_ulong,  # dwCreationDisposition
    ctypes.c_ulong,  # dwFlagsAndAttributes
    ctypes.c_void_p  # hTemplateFile
]

GetProcessId = dll.GetProcessId
GetProcessId.restype = ctypes.c_ulong
GetProcessId.argtypes = [
    ctypes.c_void_p,  # hProcess
]

LoadLibrary = dll.LoadLibraryA
LoadLibrary.restype = ctypes.c_void_p
LoadLibrary.argtypes = [
    ctypes.c_char_p,  # lpFileName
]

DeviceIoControl = dll.DeviceIoControl
DeviceIoControl.restype = ctypes.c_bool
DeviceIoControl.argtypes = [
    ctypes.c_void_p,  # hDevice
    ctypes.c_ulong,  # dwIoControlCode
    ctypes.c_void_p,  # lpInBuffer
    ctypes.c_ulong,  # nInBufferSize
    ctypes.c_void_p,  # lpOutBuffer
    ctypes.c_ulong,  # nOutBufferSize
    ctypes.c_void_p,  # lpBytesReturned
    ctypes.c_void_p,  # lpOverlapped
]

