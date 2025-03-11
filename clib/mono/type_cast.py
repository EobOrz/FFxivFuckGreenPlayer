import typing

from .defines import *
from .defines import _MonoObj

_Mono2Py = {}
_Py2Mono = {}
_SimpleCData: typing.Type = next(t for t in ctypes.c_void_p.__mro__ if '_SimpleCData' in t.__name__)
_CData: typing.Type = next(t for t in ctypes.c_void_p.__mro__ if '_CData' in t.__name__)


def _mono2py(t: MonoTypeEnum):
    def _wrapper(func):
        _Mono2Py[t] = func
        return func

    return _wrapper


def _py2mono(t: MonoTypeEnum):
    def _wrapper(func):
        _Py2Mono[t] = func
        return func

    return _wrapper


def py2mono(t: MonoTypeEnum | int, v, keeper):
    return _Py2Mono[t](v, keeper)


def mono2py(t: MonoTypeEnum | int, v):
    return _Mono2Py[t](v) if t in _Mono2Py else v


def _simple_map(t, ct):
    @_py2mono(t)
    def _(v, keeper):
        keeper.append(_v := ct(v))
        return ctypes.addressof(_v)

    @_mono2py(t)
    def _(v):
        return ct.from_address(MonoApi.get_instance().mono_object_unbox(v)).value


_simple_map(MonoTypeEnum.BOOLEAN, ctypes.c_bool)
_simple_map(MonoTypeEnum.I1, ctypes.c_int8)
_simple_map(MonoTypeEnum.U1, ctypes.c_uint8)
_simple_map(MonoTypeEnum.I2, ctypes.c_int16)
_simple_map(MonoTypeEnum.U2, ctypes.c_uint16)
_simple_map(MonoTypeEnum.I4, ctypes.c_int32)
_simple_map(MonoTypeEnum.U4, ctypes.c_uint32)
_simple_map(MonoTypeEnum.I8, ctypes.c_int64)
_simple_map(MonoTypeEnum.U8, ctypes.c_uint64)
_simple_map(MonoTypeEnum.R4, ctypes.c_float)
_simple_map(MonoTypeEnum.R8, ctypes.c_double)


@_py2mono(MonoTypeEnum.VOID)
@_py2mono(MonoTypeEnum.OBJECT)
@_py2mono(MonoTypeEnum.PTR)
@_py2mono(MonoTypeEnum.FNPTR)
@_py2mono(MonoTypeEnum.CLASS)
def _(v, keeper):
    if isinstance(v, _CData):
        return ctypes.addressof(v)
    if isinstance(v, _MonoObj):
        return v.ptr
    keeper.append(_v := ctypes.c_size_t(v))
    return ctypes.addressof(_v)


@_mono2py(MonoTypeEnum.VOID)
@_py2mono(MonoTypeEnum.OBJECT)
@_py2mono(MonoTypeEnum.PTR)
@_py2mono(MonoTypeEnum.FNPTR)
@_py2mono(MonoTypeEnum.CLASS)
def _(v):
    return v


@_py2mono(MonoTypeEnum.CHAR)
def _(v, keeper):
    if isinstance(v, _CData):
        return ctypes.addressof(v)
    if isinstance(v, str):
        v = v.encode('utf-8')
    assert isinstance(v, bytes)
    keeper.append(_v := ctypes.create_string_buffer(v))
    return ctypes.addressof(_v)


@_mono2py(MonoTypeEnum.CHAR)
def _(v):
    return ctypes.string_at(v)


@_py2mono(MonoTypeEnum.STRING)
def _(v, keeper):
    if isinstance(v, str):
        v = v.encode('utf-8')
    assert isinstance(v, bytes)
    api = MonoApi.get_instance()
    keeper.append(_v := ctypes.create_string_buffer(v))
    return api.mono_string_new(api.mono_get_root_domain(), _v)


@_mono2py(MonoTypeEnum.STRING)
def _(v):
    api = MonoApi.get_instance()
    if api.is_il2cpp:
        return api.il2cpp_string_chars(v)
    else:
        return api.mono_string_to_utf8(v).decode('utf-8')
