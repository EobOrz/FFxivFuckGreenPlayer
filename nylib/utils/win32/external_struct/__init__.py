import ctypes.wintypes
import typing

import glm

from .. import memory, process
from ..exception import WinAPIError

_addr_size = ctypes.sizeof(ctypes.c_void_p)
_T = typing.TypeVar('_T')


def _setdefault(obj, key, default):
    if key in obj.__dict__:
        return obj.__dict__[key]
    setattr(obj, key, default)
    return default


def _iter_obj_properties(owner, k):
    yield_names = set()
    for k, v in (cls_.__dict__[k].items() for cls_ in owner.__mro__ if k in cls_.__dict__):
        if k in yield_names: continue
        yield_names.add(k)
        yield k, v


class ExternalStruct:
    def __init__(self, handle, address):
        self.handle = handle
        self.address = address

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.handle}-{self.address:#x}>'


class bit_field_property:
    k = '__bit_field_property__'

    def __init__(self, offset, size=1):
        self.byte_off = offset // 8
        self.bit_off = offset % 8
        self.mask = (1 << size) - 1
        self.data_size = (self.bit_off + size + 7) // 8 * 8

    @classmethod
    def obj_properties(cls, owner):
        yield from _iter_obj_properties(owner, cls.k)

    def __set_name__(self, owner, name):
        _setdefault(owner, self.k, {})[name] = self

    def get_instance_value(self, instance):
        return getattr(memory, 'read_uint' + str(self.data_size))(instance.handle, instance.address + self.byte_off)

    def __get__(self, instance, owner):
        return (self.get_instance_value(instance) >> self.bit_off) & self.mask

    def set_instance_value(self, instance, value):
        getattr(memory, 'write_uint' + str(self.data_size))(instance.handle, instance.address + self.byte_off, value)

    def __set__(self, instance, value):
        new_val = (self.get_instance_value(instance) & ~(self.mask << self.bit_off)) | ((value & self.mask) << self.bit_off)
        self.set_instance_value(instance, new_val)


def glm_mem_property(_type: typing.Type[_T], offset_key=None, default=0) -> _T | None: ...  # dirty type hinting


class glm_mem_property(typing.Generic[_T]):
    k = '__glm_mem_property__'

    def __init__(self, t: typing.Type[_T], offset_key=None, default=0, is_static=False):
        self.t = t
        self.size = glm.sizeof(t)
        self.offset_key = offset_key
        self.default = default
        self.is_static = is_static
        self.name = None
        self.owner = None

    @classmethod
    def obj_properties(cls, owner):
        yield from _iter_obj_properties(owner, cls.k)

    def __set_name__(self, owner, name):
        self.name = name
        self.owner = owner
        if not self.offset_key: self.offset_key = name
        _setdefault(owner, self.k, {})[name] = self

    def __get__(self, instance, owner) -> _T:
        addr = 0
        if not self.is_static and not (addr := instance.address):
            return self.default
        return self.t.from_bytes(bytes(memory.read_bytes(instance.handle, addr + getattr(self.owner.offsets, self.offset_key), self.size)))

    def __set__(self, instance, value: _T):
        addr = 0
        if not self.is_static and not (addr := instance.address): return
        return memory.write_bytes(instance.handle, addr + getattr(self.owner.offsets, self.offset_key), value.to_bytes())


class direct_mem_property:
    k = '__direct_mem_property__'

    def __init__(self, _type, offset_key=None, default=0, is_static=False):
        self.type = _type
        self.offset_key = offset_key
        self.default = default
        self.is_static = is_static
        self.name = None
        self.owner = None

    @classmethod
    def obj_properties(cls, owner):
        yield from _iter_obj_properties(owner, cls.k)

    def __set_name__(self, owner, name):
        self.name = name
        self.owner = owner
        if not self.offset_key: self.offset_key = name
        _setdefault(owner, self.k, {})[name] = self

    def __get__(self, instance, owner) -> 'float | int | direct_mem_property':
        if instance is None: return self
        addr = 0
        if not self.is_static and not (addr := instance.address): return self.default
        try:
            return memory.read_memory(
                instance.handle, self.type,
                addr + getattr(self.owner.offsets, self.offset_key)).value
        except WinAPIError:
            return self.default

    def __set__(self, instance, value):
        if instance is None: return
        addr = 0
        if not self.is_static and not (addr := instance.address): return
        try:
            return memory.write_bytes(instance.handle, addr + getattr(self.owner.offsets, self.offset_key), bytearray(self.type(value)))
        except Exception:
            return


def struct_mem_property(_type: typing.Type[_T], is_pointer=False, pass_self=False, offset_key=None) -> _T | None: ...  # dirty type hinting


class struct_mem_property(typing.Generic[_T]):
    k = '__struct_mem_property__'
    cache_k = '__struct_mem_property_cache__'

    def __init__(self, _type: typing.Type[_T], is_pointer=False, pass_self: bool | str = False, offset_key=None, is_static=False):
        self.type = _type
        self.is_pointer = is_pointer
        self.pass_self = pass_self
        self.offset_key = offset_key
        self.is_static = is_static
        self.name = None
        self.owner = None

    @classmethod
    def obj_properties(cls, owner):
        yield from _iter_obj_properties(owner, cls.k)

    def __set_name__(self, owner, name):
        self.owner = owner
        self.name = name
        if not self.offset_key: self.offset_key = name
        _setdefault(owner, self.k, {})[name] = self

    def __get__(self, instance, owner) -> _T | None:
        if instance is None: return self
        cache = getattr(instance, self.cache_k, {})
        if self.name in cache: return cache[self.name]
        addr = 0
        if not self.is_static and not (addr := instance.address): return None
        addr += getattr(self.owner.offsets, self.offset_key)
        if self.is_pointer and not (addr := memory.read_address(instance.handle, addr)):
            return None
        a1 = getattr(instance, self.pass_self) if isinstance(self.pass_self, str) else instance if self.pass_self else instance.handle
        res = self.type(a1, addr)
        if not self.is_pointer:
            cache[self.name] = res
            setattr(instance, self.cache_k, cache)
        return res

    def __set__(self, instance, value):
        if instance is None: return
        addr = 0
        if not self.is_static and not (addr := instance.address): return
        addr += getattr(self.owner.offsets, self.offset_key)
        if self.is_pointer:
            memory.write_address(instance.handle, addr, value.address)
        else:
            raise TypeError('cannot set value to a non-pointer struct')
            # ny_mem.write_bytes(instance.handle, addr, value)


def generate_python_payload(res_type, arg_types):
    arg_types_ = []
    has_out_arg = False
    for i, a in enumerate(arg_types):
        if a.lower().startswith('out '):
            arg_types_.append((True, a[4:]))
            has_out_arg = True
        else:
            arg_types_.append((False, a))
    if not has_out_arg:
        return f'from ctypes import *\nres=CFUNCTYPE({res_type},{",".join(arg_types)})(args[0])(*args[1])'
    else:
        payload = f'from ctypes import *\ncargs=args[1]\n'
        call_line = f'res_=CFUNCTYPE({res_type},'
        arg_line = f')(args[0])('
        ret_line = f'res=res_,'
        carg_idx = 0
        for i, (is_out, type_) in enumerate(arg_types_):
            if is_out:
                a_idx = i + 1
                payload += f'arg{a_idx}=({type_})()\n'
                call_line += f'c_size_t,'
                arg_line += f'addressof(arg{a_idx}),'
                ret_line += f'arg{a_idx}[:],' if '*' in type_ else f'arg{a_idx}.value,'
            else:
                call_line += f'{type_},'
                arg_line += f'cargs[{carg_idx}],'
                carg_idx += 1
        return payload + call_line + arg_line + ')\n' + ret_line


class StaticFunction:
    _addr = None

    def __init__(self, addr_getter, res_type: str = None, *arg_types: str):
        self.addr_getter = addr_getter
        self.res_type = res_type
        self.arg_types = arg_types

    def get_callee(self, func_address):
        raise NotImplementedError

    def get_address(self, instance: ExternalStruct = None):
        if self._addr is None:
            self._addr = self.addr_getter() if callable(self.addr_getter) else self.addr_getter
            delattr(self, 'addr_getter')
        return self._addr

    def __get__(self, instance, owner):
        return lambda *args: self.get_callee(self.get_address(instance))(*args)

    @classmethod
    def set_callee_getter(cls, func: 'typing.Callable[[StaticFunction,int], typing.Callable'):
        StaticFunction.get_callee = func

    def __call__(self, *args):
        return self.__get__(None, None)(*args)


class ClassFunction(StaticFunction):
    def __get__(self, instance, owner):
        if instance is None:
            return lambda *args: self.get_callee(self.get_address(instance))(*args)
        else:
            return lambda *args: self.get_callee(self.get_address(instance))(instance.address, *args)


class VirtualFunction(ClassFunction):
    _vt_idx = None
    _vt_offset = None

    def __init__(self, vt_idx_getter, res_type: str, *arg_types: str, vt_offset_getter=0):
        self.vt_idx_getter = vt_idx_getter
        self.vt_offset_getter = vt_offset_getter
        super().__init__(None, res_type, *arg_types)

    def get_address(self, instance: ExternalStruct = None):
        if instance is None:
            raise TypeError('VirtualFunction cannot be called without instance')
        if self._vt_idx is None:
            self._vt_idx = self.vt_idx_getter() if callable(self.vt_idx_getter) else self.vt_idx_getter
            delattr(self, 'vt_idx_getter')
        if self._vt_offset is None:
            self._vt_offset = self.vt_offset_getter() if callable(self.vt_offset_getter) else self.vt_offset_getter
            delattr(self, 'vt_offset_getter')
        handle = instance.handle
        vtbl = memory.read_address(handle, instance.address + self._vt_offset)
        return memory.read_address(handle, vtbl + self._vt_idx * _addr_size)
