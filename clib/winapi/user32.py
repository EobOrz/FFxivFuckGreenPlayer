from .utils import *

_dll = ctypes.WinDLL('user32.dll')
OpenClipboard = def_win_api(_dll.OpenClipboard, ctypes.c_void_p, (ctypes.c_void_p,), error_zero=True)
EmptyClipboard = def_win_api(_dll.EmptyClipboard, ctypes.c_bool, (), error_zero=True)
SetClipboardData = def_win_api(_dll.SetClipboardData, ctypes.c_void_p, (ctypes.c_uint, ctypes.c_void_p), error_zero=True)
CloseClipboard = def_win_api(_dll.CloseClipboard, ctypes.c_bool, (), error_zero=True)
