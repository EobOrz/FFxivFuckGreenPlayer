import ctypes

from . import structure

dll = ctypes.WinDLL('advapi32.dll')

#: The LookupPrivilegeValue function retrieves the locally unique identifier (LUID) used on a specified system to
#: locally represent the specified privilege name.
#:
#: https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupprivilegevaluea
LookupPrivilegeValue = dll.LookupPrivilegeValueW
LookupPrivilegeValue.argtypes = (
    ctypes.c_wchar_p,  # system name
    ctypes.c_wchar_p,  # name
    ctypes.POINTER(structure.LUID),
)
LookupPrivilegeValue.restype = ctypes.c_long

#: The LookupPrivilegeName function retrieves the name that corresponds to the privilege represented on a specific
#: system by a specified locally unique identifier (LUID).
#:
#: https://docs.microsoft.com/en-us/windows/win32/api/winbase/nf-winbase-lookupprivilegenamea
LookupPrivilegeName = dll.LookupPrivilegeNameW
LookupPrivilegeName.argtypes = (
    ctypes.c_wchar_p,  # lpSystemName
    ctypes.POINTER(structure.LUID),  # lpLuid
    ctypes.c_wchar_p,  # lpName
    ctypes.POINTER(ctypes.c_ulong),  # cchName
)
LookupPrivilegeName.restype = ctypes.c_long

#: The OpenProcessToken function opens the access token associated with a process.
#:
#: https://docs.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-openprocesstoken
OpenProcessToken = dll.OpenProcessToken
OpenProcessToken.argtypes = (
    ctypes.c_void_p,
    ctypes.c_ulong,
    ctypes.POINTER(ctypes.c_void_p)
)
OpenProcessToken.restype = ctypes.c_long

#: The AdjustTokenPrivileges function enables or disables privileges in the specified access token.
#: Enabling or disabling privileges in an access token requires TOKEN_ADJUST_PRIVILEGES access.
#:
#: https://docs.microsoft.com/en-us/windows/win32/api/securitybaseapi/nf-securitybaseapi-adjusttokenprivileges
AdjustTokenPrivileges = dll.AdjustTokenPrivileges
AdjustTokenPrivileges.restype = ctypes.c_long
AdjustTokenPrivileges.argtypes = (
    ctypes.c_void_p,  # TokenHandle
    ctypes.c_long,  # DisableAllPrivileges
    structure.PTOKEN_PRIVILEGES,  # NewState (optional)
    ctypes.c_ulong,  # BufferLength of PreviousState
    structure.PTOKEN_PRIVILEGES,  # PreviousState (out, optional)
    ctypes.POINTER(ctypes.c_ulong),  # ReturnLength
)

OpenSCManagerW = dll.OpenSCManagerW
OpenSCManagerW.restype = structure.c_address
OpenSCManagerW.argtypes = (
    ctypes.c_wchar_p,  # lpMachineName
    ctypes.c_wchar_p,  # lpDatabaseName
    ctypes.c_ulong,  # dwDesiredAccess
)

OpenServiceW = dll.OpenServiceW
OpenServiceW.restype = structure.c_address
OpenServiceW.argtypes = (
    ctypes.c_void_p,  # hSCManager
    ctypes.c_wchar_p,  # lpServiceName
    ctypes.c_ulong,  # dwDesiredAccess
)

CloseServiceHandle = dll.CloseServiceHandle
CloseServiceHandle.restype = ctypes.c_bool
CloseServiceHandle.argtypes = (
    ctypes.c_void_p,  # hSCObject
)

CreateServiceW = dll.CreateServiceW
CreateServiceW.restype = structure.c_address
CreateServiceW.argtypes = (
    ctypes.c_void_p,  # hSCManager
    ctypes.c_wchar_p,  # lpServiceName
    ctypes.c_wchar_p,  # lpDisplayName
    ctypes.c_ulong,  # dwDesiredAccess
    ctypes.c_ulong,  # dwServiceType
    ctypes.c_ulong,  # dwStartType
    ctypes.c_ulong,  # dwErrorControl
    ctypes.c_wchar_p,  # lpBinaryPathName
    ctypes.c_wchar_p,  # lpLoadOrderGroup
    ctypes.c_void_p,  # lpdwTagId
    ctypes.c_wchar_p,  # lpDependencies
    ctypes.c_wchar_p,  # lpServiceStartName
    ctypes.c_wchar_p,  # lpPassword
)

DeleteService = dll.DeleteService
DeleteService.restype = ctypes.c_bool
DeleteService.argtypes = (
    ctypes.c_void_p,  # hService
)

StartService = dll.StartServiceW
StartService.restype = ctypes.c_bool
StartService.argtypes = (
    ctypes.c_void_p,  # hService
    ctypes.c_ulong,  # dwNumServiceArgs
    ctypes.c_wchar_p,  # lpServiceArgVectors
)

ControlService = dll.ControlService
ControlService.restype = ctypes.c_bool
ControlService.argtypes = (
    ctypes.c_void_p,  # hService
    ctypes.c_ulong,  # dwControl
    ctypes.POINTER(structure.SERVICE_STATUS),  # lpServiceStatus
)

OpenSCManagerW = dll.OpenSCManagerW
OpenSCManagerW.restype = structure.c_address
OpenSCManagerW.argtypes = (
    ctypes.c_wchar_p,  # lpMachineName
    ctypes.c_wchar_p,  # lpDatabaseName
    ctypes.c_ulong,  # dwDesiredAccess
)

GetSecurityInfo = dll.GetSecurityInfo
GetSecurityInfo.restype = ctypes.c_ulong
GetSecurityInfo.argtypes = (
    ctypes.c_void_p,  # handle
    ctypes.c_ulong,  # ObjectType
    ctypes.c_ulong,  # SecurityInfo
    ctypes.c_void_p,  # ppsidOwner
    ctypes.c_void_p,  # ppsidGroup
    ctypes.c_void_p,  # ppDacl
    ctypes.c_void_p,  # ppSacl
    ctypes.c_void_p,  # ppSecurityDescriptor
)
