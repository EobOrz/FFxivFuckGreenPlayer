from .utils import *

_dll = ctypes.WinDLL('ntdll.dll')
NtQueryInformationProcess = def_win_api(_dll.NtQueryInformationProcess, ctypes.c_long, (ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p), error_nt=True)
NtOpenFile = def_win_api(_dll.NtOpenFile, ctypes.c_long, (ctypes.c_void_p, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong), error_nt=True)
NtSetValueKey = def_win_api(_dll.NtSetValueKey, ctypes.c_long, (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_ulong, ctypes.c_ulong, ctypes.c_void_p, ctypes.c_ulong), error_nt=True)
RtlOpenCurrentUser = def_win_api(_dll.RtlOpenCurrentUser, ctypes.c_long, (ctypes.c_ulong, ctypes.c_void_p), error_nt=True)
