import ctypes
from . import structure

dll = ctypes.WinDLL('ntdll.dll')
NTSTATUS = structure.NTSTATUS
THREADINFOCLASS = ctypes.c_ulong

#: Retrieves information about the specified thread.
#:
#: https://msdn.microsoft.com/en-us/library/windows/desktop/ms684283.aspx
NtQueryInformationThread = dll.NtQueryInformationThread
NtQueryInformationThread.restype = NTSTATUS
NtQueryInformationThread.argtypes = [
    ctypes.c_void_p,  # ThreadHandle
    THREADINFOCLASS,  # ThreadInformationClass
    ctypes.c_void_p,  # ThreadInformation
    ctypes.c_ulong,  # ThreadInformationLength
    ctypes.POINTER(ctypes.c_ulong)  # ReturnLength
]

PROCESSINFOCLASS = ctypes.c_ulong
NtQueryInformationProcess = dll.NtQueryInformationProcess
NtQueryInformationProcess.restype = NTSTATUS
NtQueryInformationProcess.argtypes = [
    ctypes.c_void_p,  # ProcessHandle
    THREADINFOCLASS,  # ProcessInformationClass
    ctypes.c_void_p,  # ProcessInformation
    ctypes.c_ulong,  # ProcessInformationLength
    ctypes.POINTER(ctypes.c_ulong)  # ReturnLength
]

NtQuerySystemInformation = dll.NtQuerySystemInformation
NtQuerySystemInformation.restype = NTSTATUS
NtQuerySystemInformation.argtypes = [
    ctypes.c_ulong,  # SystemInformationClass
    ctypes.c_void_p,  # SystemInformation
    ctypes.c_ulong,  # SystemInformationLength
    ctypes.POINTER(ctypes.c_ulong),  # ReturnLength
]

NtQueryObject = dll.NtQueryObject
NtQueryObject.restype = NTSTATUS
NtQueryObject.argtypes = [
    ctypes.c_void_p,  # ObjectHandle
    ctypes.c_ulong,  # ObjectInformationClass
    ctypes.c_void_p,  # ObjectInformation
    ctypes.c_ulong,  # ObjectInformationLength
    ctypes.POINTER(ctypes.c_ulong),  # ReturnLength
]

# http://undocumented.ntinternals.net/index.html?page=UserMode%2FUndocumented%20Functions%2FTime%2FNtSetTimerResolution.html
NtSetTimerResolution = dll.NtSetTimerResolution
NtSetTimerResolution.restype = NTSTATUS
NtSetTimerResolution.argtypes = [
    ctypes.c_ulong,  # DesiredResolution
    ctypes.c_bool,  # SetResolution
    ctypes.POINTER(ctypes.c_ulong)  # CurrentResolution
]

NtOpenFile = dll.NtOpenFile
NtOpenFile.restype = NTSTATUS
NtOpenFile.argtypes = [
    ctypes.c_void_p,  # FileHandle
    ctypes.c_ulong,  # DesiredAccess
    ctypes.POINTER(structure.OBJECT_ATTRIBUTES),  # ObjectAttributes
    ctypes.POINTER(structure.IO_STATUS_BLOCK),  # IoStatusBlock
    ctypes.c_ulong,  # ShareAccess
    ctypes.c_ulong  # OpenOptions
]

RtlNtStatusToDosError = dll.RtlNtStatusToDosError
RtlNtStatusToDosError.restype = ctypes.c_ulong
RtlNtStatusToDosError.argtypes = [
    NTSTATUS
]

ZwDuplicateObject = dll.ZwDuplicateObject
ZwDuplicateObject.restype = NTSTATUS
ZwDuplicateObject.argtypes = [
    ctypes.c_void_p,  # SourceProcessHandle
    ctypes.c_void_p,  # SourceHandle
    ctypes.c_void_p,  # TargetProcessHandle
    ctypes.POINTER(ctypes.c_void_p),  # TargetHandle
    ctypes.c_ulong,  # DesiredAccess
    ctypes.c_ulong,  # HandleAttributes
    ctypes.c_ulong  # Options
]

ZwQuerySystemInformation = dll.ZwQuerySystemInformation
ZwQuerySystemInformation.restype = NTSTATUS
ZwQuerySystemInformation.argtypes = [
    ctypes.POINTER(ctypes.c_uint),  # SystemInformationClass
    ctypes.c_void_p,  # SystemInformation
    ctypes.c_ulong,  # SystemInformationLength
    ctypes.POINTER(ctypes.c_ulong)  # ReturnLength
]

RtlGetVersion = dll.RtlGetVersion
RtlGetVersion.restype = NTSTATUS
RtlGetVersion.argtypes = [
    ctypes.POINTER(structure.OSVERSIONINFOEXW)  # lpVersionInformation
]

ZwMapViewOfSection = dll.ZwMapViewOfSection
ZwMapViewOfSection.restype = NTSTATUS
ZwMapViewOfSection.argtypes = [
    ctypes.c_void_p,  # SectionHandle
    ctypes.c_void_p,  # ProcessHandle
    ctypes.POINTER(ctypes.c_void_p),  # BaseAddress
    ctypes.c_ulong,  # ZeroBits
    ctypes.c_ulong,  # CommitSize
    ctypes.POINTER(ctypes.c_ulonglong),  # SectionOffset
    ctypes.POINTER(ctypes.c_ulong),  # ViewSize
    ctypes.c_ulong,  # InheritDisposition
    ctypes.c_ulong,  # AllocationType
    ctypes.c_ulong  # Win32Protect
]

ZwOpenSection = dll.ZwOpenSection
ZwOpenSection.restype = NTSTATUS
ZwOpenSection.argtypes = [
    ctypes.POINTER(ctypes.c_void_p),  # SectionHandle
    ctypes.c_ulong,  # DesiredAccess
    ctypes.POINTER(structure.OBJECT_ATTRIBUTES)  # ObjectAttributes
]

ZwUnmapViewOfSection = dll.ZwUnmapViewOfSection
ZwUnmapViewOfSection.restype = NTSTATUS
ZwUnmapViewOfSection.argtypes = [
    ctypes.c_void_p,  # ProcessHandle
    ctypes.c_void_p  # BaseAddress
]
