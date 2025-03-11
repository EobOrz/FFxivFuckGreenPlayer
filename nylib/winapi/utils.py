import typing
from .defs import *

_NULL = type('NULL', (), {})
_SetLastError = ctypes.windll.kernel32.SetLastError


def def_win_api(func, res_type: typing.Any = ctypes.c_void_p, arg_types=(), error_zero=False, error_nonzero=False, error_val: typing.Any = _NULL, error_nt=False):
    func.argtypes = arg_types
    func.restype = res_type

    if error_zero:
        def wrapper(*args, **kwargs):
            _SetLastError(0)
            res = func(*args, **kwargs)
            if not res:
                raise ctypes.WinError()
            return res

        return wrapper

    if error_nonzero:
        def wrapper(*args, **kwargs):
            _SetLastError(0)
            res = func(*args, **kwargs)
            if res:
                raise ctypes.WinError()
            return res

        return wrapper

    if error_val is not _NULL:
        def wrapper(*args, **kwargs):
            _SetLastError(0)
            res = func(*args, **kwargs)
            if res == error_val:
                raise ctypes.WinError()
            return res

        return wrapper

    if error_nt:
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            if not NT_SUCCESS(res):
                raise OSError(f'NtStatus: {res:#x}')
            return res

        return wrapper
    return func
