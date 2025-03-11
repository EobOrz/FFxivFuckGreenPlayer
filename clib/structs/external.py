import ctypes
import typing

from nylib.process import Process

_T = typing.TypeVar('_T')


class ExStruct:
    _size_: int
    _need_free_: bool = False

    def __new__(cls, process: Process, address: int = None):
        self = object.__new__(cls)
        self._process_ = process
        if address is None:
            self._address_ = process.alloc(self._size_)
            self._need_free_ = True
        else:
            self._address_ = address
        return self

    def __init__(self, process: Process, address: int = None):
        self._process_ = process
        self._address_ = address

    def _free_(self):
        if self._need_free_:
            self._process_.free(self._address_, self._size_)
            self._need_free_ = False

    def __del__(self):
        self._free_()

    def __repr__(self):
        return f'<{self.__class__.__name__} at process={self._process_.process_id} address={self._address_:#X}>'


class ExField:
    def __init__(self, type: typing.Type[_T], offset: int | str = None):
        self.type = type
        self._is_exstruct = issubclass(type, ExStruct)
        if isinstance(offset, str):
            self._offset = None
            self._name = offset
        else:
            self._offset = offset
            self._name = None

    def __set_name__(self, owner, name):
        if self._name is None:
            self._name = name

    def get_offset(self, instance: ExStruct):
        if self._offset is None:
            return getattr(getattr(instance, '_offset_'), self._name)
        return self._offset

    def __get__(self, instance: ExStruct, owner=None) -> _T:
        offset = self.get_offset(instance)
        address = instance._address_ + offset
        if self._is_exstruct:
            return self.type(instance._process_, address)
        return instance._process_.read(address, self.type)

    def __set__(self, instance: ExStruct, value: _T):
        offset = self.get_offset(instance)
        address = instance._address_ + offset
        if self._is_exstruct:
            instance._process_.write(address, value._process_.read(value._address_, value._size_))
        instance._process_.write(instance._address_ + offset, value)


class ExFieldSimp(ExField):
    def __get__(self, instance: ExStruct, owner=None) -> typing.Any:
        return super().__get__(instance, owner).value


class _ExIterable(ExStruct, typing.Generic[_T]):
    _type_: typing.Type[_T]
    _length_: int

    @classmethod
    def _type_size_(cls):
        return cls._type_._size_ if issubclass(cls._type_, ExStruct) else ctypes.sizeof(cls._type_)

    @typing.overload
    def __getitem__(self, index: slice) -> tuple[_T, ...]:
        ...

    @typing.overload
    def __getitem__(self, index: int) -> _T:
        ...

    def _first_at_(self) -> int:
        raise NotImplementedError

    def _item_at_(self, index) -> int:
        if not (addr := self._first_at_()):
            return 0
        if index < 0:
            raise IndexError('Index out of range')
        if index > 0:
            addr += index * self._type_size_()
        return addr

    def __getitem__(self, index) -> _T:
        if isinstance(index, slice):
            return tuple(self[i] for i in range(*index.indices(self._length_)))
        elif isinstance(index, int):
            if not (addr := self._item_at_(index)): return None
            if issubclass(self._type_, ExStruct):
                return self._type_(self._process_, addr)
            return self._process_.read(addr, self._type_)
        else:
            raise TypeError(f'Invalid index type:{type(index)}')

    def __setitem__(self, index, value):
        if isinstance(index, slice):
            for i, v in zip(range(*index.indices(self._length_)), value):
                self[i] = v
        elif isinstance(index, int):
            if not (addr := self._item_at_(index)): raise IndexError('Writing to invalid address')
            if issubclass(self._type_, ExStruct):
                self._process_.write(addr, value._process_.read(value._address_, value._size_))
            else:
                self._process_.write(addr, value)
        else:
            raise TypeError(f'Invalid index type:{type(index)}')

    def __iter__(self):
        if hasattr(self, '_length_'):
            for i in range(self._length_):
                yield self[i]
        else:
            i = 0
            while True:
                yield self[i]
                i += 1


class ExPtr(_ExIterable[_T]):
    _size_ = ctypes.sizeof(ctypes.c_void_p)

    def __class_getitem__(cls, item) -> 'ExPtr[_T]':
        assert not hasattr(cls, '_type_')
        return type(f'ExPtr[{item.__name__}]', (cls,), {'_type_': item})

    def _first_at_(self) -> int:
        return self._process_.read_ptr(self._address_)

    def __bool__(self):
        return bool(self._first_at_())

    @property
    def value(self) -> _T:
        return self[0]

    @value.setter
    def value(self, value: _T):
        self[0] = value


class ExArr(_ExIterable[_T]):

    def __class_getitem__(cls, item) -> 'ExArr[_T]':
        assert not hasattr(cls, '_type_')
        if isinstance(item, tuple):
            item, length = item
            return type(f'ExArr[{item.__name__}]', (cls,), {'_type_': item, '_length_': length})
        return type(f'ExArr[{item.__name__}]', (cls,), {'_type_': item})

    @property
    def _size_(self) -> int:
        return self._type_size_() * self._length_

    def __first_at_(self) -> int:
        return self._address_


class ExStringPointer(ExStruct):
    _encoding_: str = 'utf-8'

    @property
    def value(self):
        return self._process_.read_string(self._process_.read_ptr(self._address_), encoding=self._encoding_)


class ExVfunc:
    def __init__(self, idx: int):
        self.idx = idx

    def __get__(self, instance, owner):
        p_vtbl = instance._process_.read_ptr(instance._address_)
        p_func = instance._process_.read_ptr(p_vtbl + self.idx * ctypes.sizeof(ctypes.c_void_p))
        return lambda *a: instance._process_.call(p_func, instance._address_, *a)


class ExStaticFunc:
    def __init__(self, address_getter):
        self.address_getter = address_getter

    def get_address(self, process: Process):
        if not hasattr(process, '_ex_static_func_cache_'):
            process._ex_static_func_cache_ = c = {}
        else:
            c = process._ex_static_func_cache_
        if not id(self) in c:
            c[id(self)] = res = self.address_getter(process)
        else:
            res = c[id(self)]
        return res

    def __get__(self, instance, owner):
        return lambda *a: instance._process_.call(self.get_address(instance._process_), instance._address_, *a)
