"""
A module to access memory with ctypes, but different from ctypes,
this module allow to use custom native accessors, so it can be used to access memory of other process
"""

import ctypes
import functools
import operator
import struct
import typing

from .memory_manage import MemoryManager
from .. import winapi
from ..utils import mv_from_mem

if typing.TYPE_CHECKING:
    from ..process import Process

_T = typing.TypeVar("_T")
struct_u64 = struct.Struct("Q")
struct_ptr = struct_u64


def size_padded(size: int, pad_size: int) -> int:
    if pad_size < 2: return size
    v = pad_size - 1
    return (size + v) & ~v


class CDataMeta(type):
    def __mul__(cls: typing.Type[_T], n: int) -> 'typing.Type[Array[_T]]':
        return Array[cls, n]


class CData(metaclass=CDataMeta):
    _accessor_: 'CAccessor'
    _address_: int
    _size_: int
    _pad_size_: int
    _can_self_handle_: bool = False
    _is_self_allocated_: bool = False

    def __del__(self):
        if self._is_self_allocated_:
            self._accessor_.free(self._address_)

    def __init__(self, *args, _address_=None, _accessor_=None, **kwargs):
        self._accessor_ = _accessor_ or CAccessorLocal.get_instance()
        if _address_ is not None:
            self._address_ = _address_
        elif self._can_self_handle_:
            self._address_ = self._accessor_.alloc(self._size_)
            self._is_self_allocated_ = True
        else:
            raise ValueError("Can't self handle")


_CData_T = typing.TypeVar("_CData_T", bound=CData)


def cdata_from_buffer_copy(buf: bytes, t: typing.Type[_CData_T], _accessor_: 'CAccessor' = None) -> _CData_T:
    obj = t(_accessor_=_accessor_)
    obj._accessor_.write(obj._address_, buf)
    return obj


def cdata_from_buffer(buf: bytearray, t: typing.Type[_CData_T], offset=0) -> _CData_T:
    buf_ = (ctypes.c_char * len(buf)).from_buffer(buf)
    obj = t(_address_=ctypes.addressof(buf_) + offset, _accessor_=CAccessorLocal.get_instance())
    obj._raw_buf_ = buf_
    return obj


def check_finalize(t: typing.Type[CData] | CData):
    if not isinstance(t, type):
        t = type(t)
    if issubclass(t, Struct):
        if not hasattr(t, "_fields_"):
            finalize_struct(t)


def sizeof(t: typing.Type[CData] | CData) -> int:
    check_finalize(t)
    return t._size_


def padsizeof(t: typing.Type[CData] | CData) -> int:
    check_finalize(t)
    return t._pad_size_


class SimpleCDataMeta(CDataMeta):
    def __mul__(cls: 'typing.Type[SimpleCData[_T]]', n: int) -> 'typing.Type[SArray[_T]]':
        return SArray[cls, n]


class SimpleCData(CData, typing.Generic[_T], metaclass=SimpleCDataMeta):
    _can_self_handle_ = True
    _struct_: struct.Struct
    _struct__: str
    _ctype_: typing.Type
    _is_xmm_: bool = False

    def __init_subclass__(cls, **kwargs):
        if s := getattr(cls, "_struct__", None):
            cls._struct_ = struct.Struct(s)
        if getattr(cls, "_struct_", None):
            cls._pad_size_ = cls._size_ = cls._struct_.size

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if args: self.value = args[0]

    @property
    def value(self) -> _T:
        return self._struct_.unpack(self._accessor_.read(self._address_, self._struct_.size))[0]

    @value.setter
    def value(self, value: _T):
        if isinstance(value, bytes):
            pass
        else:
            if isinstance(value, SimpleCData): value = value.value
            value = self._struct_.pack(value)
        self._accessor_.write(self._address_, value)

    def _op_(self, other, op):
        return op(self.value, other.value if isinstance(other, SimpleCData) else other)

    def _iop_(self, other, op):
        self.value = op(self.value, other.value if isinstance(other, SimpleCData) else other)
        return self

    __eq__ = lambda self, other: self._op_(other, operator.eq)
    __ne__ = lambda self, other: self._op_(other, operator.ne)
    __lt__ = lambda self, other: self._op_(other, operator.lt)
    __le__ = lambda self, other: self._op_(other, operator.le)
    __gt__ = lambda self, other: self._op_(other, operator.gt)
    __ge__ = lambda self, other: self._op_(other, operator.ge)
    __add__ = lambda self, other: self._op_(other, operator.add)
    __sub__ = lambda self, other: self._op_(other, operator.sub)
    __mul__ = lambda self, other: self._op_(other, operator.mul)
    __truediv__ = lambda self, other: self._op_(other, operator.truediv)
    __floordiv__ = lambda self, other: self._op_(other, operator.floordiv)
    __mod__ = lambda self, other: self._op_(other, operator.mod)
    __pow__ = lambda self, other: self._op_(other, operator.pow)
    __lshift__ = lambda self, other: self._op_(other, operator.lshift)
    __rshift__ = lambda self, other: self._op_(other, operator.rshift)
    __and__ = lambda self, other: self._op_(other, operator.and_)
    __xor__ = lambda self, other: self._op_(other, operator.xor)
    __or__ = lambda self, other: self._op_(other, operator.or_)
    __iadd__ = lambda self, other: self._iop_(other, operator.iadd)
    __isub__ = lambda self, other: self._iop_(other, operator.isub)
    __imul__ = lambda self, other: self._iop_(other, operator.imul)
    __itruediv__ = lambda self, other: self._iop_(other, operator.itruediv)
    __ifloordiv__ = lambda self, other: self._iop_(other, operator.ifloordiv)
    __imod__ = lambda self, other: self._iop_(other, operator.imod)
    __ipow__ = lambda self, other: self._iop_(other, operator.ipow)
    __ilshift__ = lambda self, other: self._iop_(other, operator.ilshift)
    __irshift__ = lambda self, other: self._iop_(other, operator.irshift)
    __iand__ = lambda self, other: self._iop_(other, operator.iand)
    __ixor__ = lambda self, other: self._iop_(other, operator.ixor)
    __ior__ = lambda self, other: self._iop_(other, operator.ior)


class c_uint8(SimpleCData[int]):
    _struct__ = "B"
    _ctype_ = ctypes.c_uint8


class c_uint16(SimpleCData[int]):
    _struct__ = "H"
    _ctype_ = ctypes.c_uint16


class c_uint32(SimpleCData[int]):
    _struct__ = "I"
    _ctype_ = ctypes.c_uint32


class c_uint64(SimpleCData[int]):
    _struct__ = "Q"
    _ctype_ = ctypes.c_uint64


class c_int8(SimpleCData[int]):
    _struct__ = "b"
    _ctype_ = ctypes.c_int8


class c_int16(SimpleCData[int]):
    _struct__ = "h"
    _ctype_ = ctypes.c_int16


class c_int32(SimpleCData[int]):
    _struct__ = "i"
    _ctype_ = ctypes.c_int32


class c_int64(SimpleCData[int]):
    _struct__ = "q"
    _ctype_ = ctypes.c_int64


class c_float(SimpleCData[float]):
    _struct__ = "f"
    _ctype_ = ctypes.c_float
    _is_xmm_ = True


class c_double(SimpleCData[float]):
    _struct__ = "d"
    _ctype_ = ctypes.c_double
    _is_xmm_ = True


class c_char(SimpleCData[bytes]):
    _pad_size_ = _size_ = 1

    def __class_getitem__(cls, size: int):
        return type(f'c_char_{size}', (c_char,), {"_size_": size})

    @property
    def value(self) -> bytes:
        return self._accessor_.read(self._address_, self._size_)

    @value.setter
    def value(self, value: bytes):
        if len(value) >= self._size_:
            value = value[:self._size_]
        self._accessor_.write(self._address_, value)


class c_char_zt(SimpleCData[bytes]):
    _pad_size_ = _size_ = 1

    def __class_getitem__(cls, size: int):
        return type(f'c_char_zt_{size}', (c_char_zt,), {"_size_": size})

    @property
    def value(self) -> bytes:
        res = self._accessor_.read(self._address_, self._size_)
        if (i := res.find(0)) >= 0:
            res = res[:i]
        return res

    @value.setter
    def value(self, value: bytes):
        if len(value) >= self._size_:
            value = value[:self._size_]
        self._accessor_.write(self._address_, value)


class c_wchar(SimpleCData[str]):
    encoding = "utf-16-le"
    _pad_size_ = _size_ = 2

    def __class_getitem__(cls, item: int | tuple[int, str]):
        if isinstance(item, tuple):
            size, encoding = item
            return type(f'c_wchar_{size}', (c_wchar,), {"_size_": size, "encoding": encoding})
        return type(f'c_wchar_{item}', (c_wchar,), {"_size_": item})

    @property
    def value(self) -> str:
        return self._accessor_.read(self._address_, self._size_).decode(self.encoding)

    @value.setter
    def value(self, value: str):
        if len(value) >= self._size_:
            value = value[:self._size_]
        self._accessor_.write(self._address_, value.encode(self.encoding))


class c_wchar_zt(SimpleCData[str]):
    encoding = "utf-16-le"
    _pad_size_ = _size_ = 2

    def __class_getitem__(cls, item: int | tuple[int, str]):
        if isinstance(item, tuple):
            size, encoding = item
            return type(f'c_wchar_zt_{size}', (c_wchar_zt,), {"_size_": size, "encoding": encoding})
        return type(f'c_wchar_zt_{item}', (c_wchar_zt,), {"_size_": item})

    @property
    def value(self) -> str:
        res = self._accessor_.read(self._address_, self._size_)
        for i in range(0, len(res), 2):
            if res[i:i + 2] == b"\x00\x00":
                res = res[:i]
                break
        return res.decode(self.encoding)

    @value.setter
    def value(self, value: str):
        if len(value) >= self._size_:
            value = value[:self._size_]
        self._accessor_.write(self._address_, value.encode(self.encoding))


c_size_t = c_uint64
c_longlong = c_int64
c_ulonglong = c_uint64
c_long = c_int32
c_ulong = c_uint32
c_int = c_int32
c_uint = c_uint32
c_short = c_int16
c_ushort = c_uint16
c_void_p = c_uint64


class Pointer(CData, typing.Generic[_CData_T]):
    _pad_size_ = _size_ = c_size_t._size_
    _type_: typing.Type[_CData_T]
    _can_self_handle_ = True

    def __init__(self, value=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if value: self.value = value

    @property
    def value(self) -> _CData_T:
        return struct_ptr.unpack(self._accessor_.read(self._address_, struct_ptr.size))[0]

    @value.setter
    def value(self, value: _CData_T):
        if isinstance(value, bytes):
            pass
        else:
            if isinstance(value, SimpleCData): value = value.value
            value = struct_ptr.pack(value)
        self._accessor_.write(self._address_, value)

    @property
    def content(self) -> _CData_T:
        return self[0]

    @functools.cached_property
    def element_size_padded(self) -> int:
        return size_padded(sizeof(self._type_), padsizeof(self._type_))

    def __getitem__(self, item: int) -> _CData_T:
        return self._type_(_address_=self.value + item * self.element_size_padded, _accessor_=self._accessor_)

    def __class_getitem__(cls, t: typing.Type[_CData_T]) -> 'Pointer[_CData_T]':
        return type(f'p_{t.__name__}', (cls,), {"_type_": t})


class c_char_p(Pointer[c_char]):
    def __init__(self, value=None, *args, **kwargs):
        if value is not None:
            if isinstance(value, str):
                value = value.encode("utf-8") + b"\x00"
            elif isinstance(value, bytes):
                if value[-1] != 0: value += b"\x00"
            else:
                raise ValueError("Value must be bytes or str")
        super().__init__(None, *args, **kwargs)
        if value is not None:
            self.value = a = self._accessor_.alloc(len(value))
            self._accessor_.write(a, value)

    @property
    def content(self) -> bytes:
        return ctypes.string_at(self.value)


class Array(CData, typing.Generic[_CData_T]):
    _type_: typing.Type[_CData_T]
    _length_: int

    def __getitem__(self, item: int) -> _CData_T:
        if 0 <= self._length_ <= item: raise IndexError
        return self._type_(_address_=self._address_ + item * self.element_size_padded, _accessor_=self._accessor_)

    def __iter__(self) -> typing.Iterator[_CData_T]:
        ptr = self._address_
        ps = self.element_size_padded
        if self._length_ < 0:
            while True:
                yield self._type_(_address_=ptr, _accessor_=self._accessor_)
                ptr += ps
        else:
            for _ in range(self._length_):
                yield self._type_(_address_=ptr, _accessor_=self._accessor_)
                ptr += ps

    @functools.cached_property
    def element_size_padded(self) -> int:
        return size_padded(sizeof(self._type_), padsizeof(self._type_))

    def __class_getitem__(cls, t: typing.Type[_CData_T] | tuple[typing.Type[_CData_T], int]) -> 'typing.Type[Array[_CData_T]]':
        if isinstance(t, tuple):
            t, length = t
            size = size_padded(sizeof(t), padsizeof(t)) * length
            can_self_handle = t._can_self_handle_
        else:
            length = -1
            size = 0
            can_self_handle = False
        return type(f'a_{t.__name__}', (cls,), {
            "_type_": t,
            "_length_": length,
            "_size_": size,
            "_pad_size_": t._pad_size_,
            "_can_self_handle_": can_self_handle
        })


class SArray(CData, typing.Generic[_T]):
    _type_: typing.Type[SimpleCData[_T]]
    _length_: int

    def _raw_get(self, item: int) -> SimpleCData[_T]:
        if 0 <= self._length_ <= item: raise IndexError
        return self._type_(_address_=self._address_ + item * self.element_size_padded, _accessor_=self._accessor_)

    def __getitem__(self, item: int) -> _T:
        return self._raw_get(item).value

    def __setitem__(self, item: _T, value):
        self._raw_get(item).value = value

    def __iter__(self) -> typing.Iterator[_T]:
        ptr = self._address_
        ps = self.element_size_padded
        if self._length_ < 0:
            while True:
                yield self._type_(_address_=ptr, _accessor_=self._accessor_).value
                ptr += ps
        else:
            for _ in range(self._length_):
                yield self._type_(_address_=ptr, _accessor_=self._accessor_).value
                ptr += ps

    @functools.cached_property
    def element_size_padded(self) -> int:
        return size_padded(sizeof(self._type_), padsizeof(self._type_))

    def __class_getitem__(cls, t: typing.Type[SimpleCData[_T]] | tuple[typing.Type[SimpleCData[_T]], int]) -> 'typing.Type[SArray[_T]]':
        if isinstance(t, tuple):
            t, length = t
            size = size_padded(sizeof(t), padsizeof(t)) * length
            can_self_handle = t._can_self_handle_
        else:
            length = -1
            size = 0
            can_self_handle = False
        return type(f'sa_{t.__name__}', (cls,), {
            "_type_": t,
            "_length_": length,
            "_size_": size,
            "_pad_size_": t._pad_size_,
            "_can_self_handle_": can_self_handle
        })


def finalize_struct(cls):
    fields = []

    for name, t in cls.__dict__.items():
        if isinstance(t, Field):
            assert not hasattr(t, "name"), "Field name is reserved"
            t.name = name
            fields.append(t)

    size = 0
    pad_size = 1
    i = 0
    while i < len(fields):
        field = fields[i]
        field_size = sizeof(field.t)
        if field.offset < 0:
            field.offset = size = size_padded(size, padsizeof(field.t))
            size += field_size
        else:
            size = max(field.offset + field_size, size)
        pad_size = max(pad_size, padsizeof(field.t))
        i += 1
        if isinstance(field, BField):
            bit_max = field_size * 8
            if field.bit_offset < 0:
                field.bit_offset = 0
            bit_cur = field.bit_offset + field.bit_size
            while i < len(fields):
                next_field = fields[i]
                if not isinstance(next_field, BField): break
                if next_field.t != field.t: break
                if next_field.offset > field.offset:
                    break
                elif next_field.offset < 0:
                    if next_field.bit_offset < 0:
                        if bit_cur + next_field.bit_size > bit_max: break
                        next_field.bit_offset = bit_cur
                    else:
                        if next_field.bit_offset > next_field.bit_offset: break
                    next_field.offset = field.offset
                elif next_field.offset < field.offset:
                    assert next_field.bit_offset >= 0, "Bit offset must be set for backward bit field"
                    break
                else:  # next_field.offset == field.offset
                    if next_field.bit_offset < 0:
                        if bit_cur + next_field.bit_size > bit_max:
                            raise ValueError("Bit field overflow")
                        next_field.bit_offset = bit_cur
                    else:
                        if next_field.bit_offset > next_field.bit_offset:
                            raise ValueError("Bit field overflow")
                bit_cur = max(bit_cur, next_field.bit_offset + next_field.bit_size)
                i += 1

    cls._fields_ = fields
    cls._size_ = max(size, getattr(cls, "_size_", 0))
    cls._pad_size_ = pad_size


class Struct(CData):
    _fields_: 'list[Field]'
    _can_self_handle_ = True


class Field(typing.Generic[_T]):
    name: str

    def __init__(self, t: typing.Type[_T], offset: int = -1):
        assert issubclass(t, CData), "Field type must be subclass of CData"
        self.t = t
        self.offset = offset

    def __get__(self, instance: Struct, owner) -> _T:
        if self.offset < 0: finalize_struct(owner)
        return self.t(_address_=instance._address_ + self.offset, _accessor_=instance._accessor_)


class SField(Field[_T]):
    def __init__(self, t: typing.Type[SimpleCData[_T]], offset: int = -1):
        assert issubclass(t, SimpleCData), "Field type must be subclass of SimpleCData"
        super().__init__(t, offset)

    def __get__(self, instance: Struct, owner) -> _T:
        return super().__get__(instance, owner).value

    def __set__(self, instance: Struct, value: _T):
        super().__get__(instance, instance.__class__).value = value


class BField(Field[int]):
    rev_mask: int = -1  # fill when finalize ~(self.bit_mask << self.bit_offset)

    def __init__(self, t: typing.Type[SimpleCData[int]], bit_size: int = 1, offset: int = -1, bit_offset: int = -1):
        assert issubclass(t, SimpleCData), "Field type must be subclass of SimpleCData"
        super().__init__(t, offset)
        self.bit_size = bit_size
        self.bit_offset = bit_offset
        self.bit_mask = (1 << bit_size) - 1

    def __get__(self, instance: Struct, owner) -> int:
        if self.bit_offset < 0: finalize_struct(owner)
        return (super().__get__(instance, owner).value >> self.bit_offset) & self.bit_mask

    def __set__(self, instance: Struct, value: int):
        if self.bit_offset < 0 or self.bit_size < 0: finalize_struct(instance.__class__)
        _value = super().__get__(instance, instance.__class__)
        _value.value = (_value.value & self.rev_mask) | ((value & self.bit_mask) << self.bit_offset)


class FuncDecl:
    shell: bytes

    def __init__(self, restype, *argtypes):
        self.restype = restype
        self.argtypes = argtypes

    def make_param(self, address, *args):
        raise NotImplementedError

    def __call__(self, address, *args, **kwargs):  # TODO: add support for expose python function?
        return CFunction(self, _address_=address, *args, **kwargs)


class FastCall(FuncDecl):
    # shell = keystone.Ks(keystone.KS_ARCH_X86, keystone.KS_MODE_64).asm(
    #     "push rbp;"
    #     "mov rbp, rsp;"
    #     "push rsi;"
    #     "push rdi;"
    #     "mov rbx, rcx;"
    #     "mov rcx, [rbx + 0x48];"
    #     "lea rsi, [rbx + 0x50]"
    #     "sub rsp, rcx;"
    #     "mov rdi, rsp;"
    #     "rep movsb;"
    #     "sub rsp, 0x20;"
    #     "mov rcx, [rbx + 0x8];"
    #     "mov rdx, [rbx + 0x10];"
    #     "mov r8, [rbx + 0x18];"
    #     "mov r9, [rbx + 0x20];"
    #     "movq xmm0, [rbx + 0x28];"
    #     "movq xmm1, [rbx + 0x30];"
    #     "movq xmm2, [rbx + 0x38];"
    #     "movq xmm3, [rbx + 0x40];"
    #     "call [rbx];"
    #     "pop rdi;"
    #     "pop rsi;"
    #     "mov rsp, rbp;"
    #     "pop rbp;"
    #     "ret;", as_bytes=True)[0]
    shell = bytes.fromhex("554889e556574889cb488b4b48488d73504829cc4889e7f3a44883ec20488b4b08488b53104c8b43184c8b4b20f30f7e4328f30f7e4b30f30f7e5338f30f7e5b40ff135f5e4889ec5dc3")

    def __init__(self, restype, *argtypes):
        super().__init__(restype, *argtypes)
        self.stack_size = 0
        if len(argtypes) > 4:
            self.stack_size = len(argtypes) * 8
            self.stack_size = (self.stack_size + 0xf) & ~0xf

    def make_param(self, address, *args):
        assert len(args) == len(self.argtypes)
        buf = bytearray(0x50 + self.stack_size)
        data = bytearray()
        need_fix_ptr = []
        struct_u64.pack_into(buf, 0, address)
        if self.stack_size:
            struct_u64.pack_into(buf, 0x48, self.stack_size)
        for i, (arg, t) in enumerate(zip(args, self.argtypes)):
            if issubclass(t, SimpleCData):
                if i < 4:
                    if t._is_xmm_:
                        t._struct_.pack_into(buf, 0x28 + i * 8, arg)
                    else:
                        t._struct_.pack_into(buf, 0x8 + i * 8, arg)
                else:
                    t._struct_.pack_into(buf, (0x50 - 0x20) + i * 8, arg)
                continue
            off = 0x8 + i * 8 if i < 4 else (0x50 - 0x20) + i * 8
            if issubclass(t, c_char_p) and isinstance(arg, (str, bytes)):
                if isinstance(arg, str):
                    arg = arg.encode("utf-8") + b"\x00"
                elif arg[-1] != 0:
                    arg += b"\x00"
                struct_u64.pack_into(buf, off, len(buf) + len(data))
                data += arg
                need_fix_ptr.append(off)
            elif issubclass(t, Pointer):
                if isinstance(arg, Pointer):
                    struct_u64.pack_into(buf, off, arg.value)
                elif isinstance(arg, CData):
                    struct_u64.pack_into(buf, off, arg._address_)
                elif isinstance(arg, int):
                    struct_u64.pack_into(buf, off, arg)
                else:
                    raise ValueError("Invalid argument")

        return buf + data, need_fix_ptr


class CFunction(CData):  # TODO: pointer? or shell?
    _size_: int = c_size_t._size_
    _pad_size_: int = c_size_t._size_

    def __init__(self, func_decl: FuncDecl, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.func_decl = func_decl

    def __call__(self, *args):
        return self._accessor_.call(self.func_decl, self._address_, *args)


class CAccessor:
    def read(self, address: int, size: int) -> bytes:
        raise NotImplementedError

    def write(self, address: int, value: bytes):
        raise NotImplementedError

    def call(self, func_decl, address: int, *args):
        raise NotImplementedError

    def alloc(self, size: int) -> int:
        raise NotImplementedError

    def free(self, address: int):
        raise NotImplementedError

    def alloc_exec(self, size: int) -> int:
        raise NotImplementedError

    def free_exec(self, address: int):
        raise NotImplementedError


class CAccessorLocal(CAccessor):
    @classmethod
    def get_instance(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        self._alloc = {}
        self._alloc_exec = {}
        self._shells = {}
        self.shell_buffer = MemoryManager(self.alloc_exec, self.free_exec)

    def __del__(self):
        while self._alloc_exec:
            self.free_exec(next(iter(self._alloc_exec)))

    def read(self, address: int, size: int) -> bytes:
        return bytes(mv_from_mem(address, size, 0x100))

    def write(self, address: int, value: bytes):
        mv_from_mem(address, len(value), 0x200)[:] = value

    def call(self, func_decl: FuncDecl, address: int, *args):
        param, need_fix_ptr = func_decl.make_param(address, *args)
        buf = (ctypes.c_char * len(param)).from_buffer(param)
        a_buf = ctypes.addressof(buf)
        for off in need_fix_ptr:
            struct_u64.pack_into(param, off, a_buf + struct_u64.unpack_from(param, off)[0])
        func_decl_t = type(func_decl)
        key = id(func_decl_t)
        if not (ptr := self._shells.get(key)):
            shell = func_decl_t.shell
            self._shells[key] = ptr = self.shell_buffer.alloc(len(shell))
            self.write(ptr, shell)

        res_t = func_decl.restype
        if res_t is c_float:
            return ctypes.CFUNCTYPE(ctypes.c_float, ctypes.c_char_p)(ptr)(buf)
        elif res_t is c_double:
            return ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_char_p)(ptr)(buf)
        else:
            res = ctypes.CFUNCTYPE(ctypes.c_uint64, ctypes.c_char_p)(ptr)(buf)
            if issubclass(res_t, SimpleCData):
                return res_t._struct_.unpack(struct_u64.pack(res))[0]
            return res_t(_address_=res, _accessor_=self)

    def alloc(self, size: int) -> int:
        buf = ctypes.create_string_buffer(size)
        address = ctypes.addressof(buf)
        self._alloc[address] = buf
        return address

    def free(self, address: int):
        del self._alloc[address]

    def alloc_exec(self, size: int) -> int:
        address = winapi.VirtualAllocEx(-1, 0, size, 0x3000, 0x40)
        self._alloc_exec[address] = size
        return address

    def free_exec(self, address: int):
        del self._alloc_exec[address]
        winapi.VirtualFreeEx(-1, address, 0, 0x8000)


class CAccessorProcess(CAccessor):
    def __init__(self, process: 'Process'):
        self.process = process
        self._shells = {}
        self.shell_buffer = MemoryManager(self.alloc_exec, self.free_exec)

    def read(self, address: int, size: int) -> bytes:
        return self.process.read(address, size)

    def write(self, address: int, value: bytes):
        self.process.write(address, value)

    def call(self, func_decl: FuncDecl, address: int, *args):
        func_decl_t = type(func_decl)
        key = id(func_decl_t)
        if not (ptr := self._shells.get(key)):
            shell = func_decl_t.shell
            self._shells[key] = ptr = self.shell_buffer.alloc(len(shell))
            self.write(ptr, shell)

        param, need_fix_ptr = func_decl.make_param(address, *args)
        abuf = self.alloc(len(param))
        for off in need_fix_ptr:
            struct_u64.pack_into(param, off, abuf + struct_u64.unpack_from(param, off)[0])
        self.write(abuf, param)

        res_t = func_decl.restype
        res_is_xmm = res_t is c_float or res_t is c_double
        # TODO: use better shell
        res = self.process.call(ptr, abuf, read_xmm=res_is_xmm, get_bytes=True)
        if issubclass(res_t, SimpleCData):
            return res_t._struct_.unpack_from(res)[0]
        return res_t(_address_=res, _accessor_=self)

    def alloc(self, size: int) -> int:
        return self.process.alloc(size, protect=0x04)

    def free(self, address: int):
        self.process.free(address)

    def alloc_exec(self, size: int) -> int:
        return self.process.alloc(size, protect=0x40)

    def free_exec(self, address: int):
        self.process.free(address)
