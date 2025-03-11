from .utils import *

_dll = ctypes.WinDLL('advapi32.dll')
OpenProcessToken = def_win_api(_dll.OpenProcessToken, ctypes.c_long, (ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p), error_zero=True)
LookupPrivilegeName = def_win_api(_dll.LookupPrivilegeNameW, ctypes.c_long, (ctypes.c_wchar_p, ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_void_p), error_zero=True)
LookupPrivilegeValue = def_win_api(_dll.LookupPrivilegeValueW, ctypes.c_long, (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_void_p), error_zero=True)
AdjustTokenPrivileges = def_win_api(_dll.AdjustTokenPrivileges, ctypes.c_long, (ctypes.c_void_p, ctypes.c_long, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p), error_zero=True)
OpenSCManagerW = def_win_api(_dll.OpenSCManagerW, ctypes.c_void_p, (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32), error_zero=True)
CloseServiceHandle = def_win_api(_dll.CloseServiceHandle, ctypes.c_void_p, (ctypes.c_void_p,), error_zero=True)
CreateServiceW = def_win_api(_dll.CreateServiceW, ctypes.c_void_p, (
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
), error_zero=True)
CreateServiceA = def_win_api(_dll.CreateServiceA, ctypes.c_void_p, (
    ctypes.c_void_p,  # hSCManager
    ctypes.c_char_p,  # lpServiceName
    ctypes.c_char_p,  # lpDisplayName
    ctypes.c_ulong,  # dwDesiredAccess
    ctypes.c_ulong,  # dwServiceType
    ctypes.c_ulong,  # dwStartType
    ctypes.c_ulong,  # dwErrorControl
    ctypes.c_char_p,  # lpBinaryPathName
    ctypes.c_char_p,  # lpLoadOrderGroup
    ctypes.c_void_p,  # lpdwTagId
    ctypes.c_char_p,  # lpDependencies
    ctypes.c_char_p,  # lpServiceStartName
    ctypes.c_char_p,  # lpPassword
), error_zero=True)
ChangeServiceConfigW = def_win_api(_dll.ChangeServiceConfigW, ctypes.c_bool, (
    ctypes.c_void_p,  # hService
    ctypes.c_ulong,  # dwServiceType
    ctypes.c_ulong,  # dwStartType
    ctypes.c_ulong,  # dwErrorControl
    ctypes.c_wchar_p,  # lpBinaryPathName
    ctypes.c_wchar_p,  # lpLoadOrderGroup
    ctypes.c_void_p,  # lpdwTagId
    ctypes.c_wchar_p,  # lpDependencies
    ctypes.c_wchar_p,  # lpServiceStartName
    ctypes.c_wchar_p,  # lpPassword
    ctypes.c_wchar_p,  # lpDisplayName
), error_zero=True)
OpenServiceW = def_win_api(_dll.OpenServiceW, ctypes.c_void_p, (ctypes.c_void_p, ctypes.c_wchar_p, ctypes.c_ulong), error_zero=True)
ControlService = def_win_api(_dll.ControlService, ctypes.c_bool, (ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p), error_zero=True)
StartService = def_win_api(_dll.StartServiceW, ctypes.c_bool, (ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p), error_zero=True)
DeleteService = def_win_api(_dll.DeleteService, ctypes.c_bool, (ctypes.c_void_p,), error_zero=True)
