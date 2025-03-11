from .utils import *

_dll = ctypes.CDLL('msvcrt.dll')
memcpy = def_win_api(_dll.memcpy, ctypes.c_void_p, (ctypes.c_void_p, ctypes.c_void_p, ctypes.c_size_t), error_zero=True)
