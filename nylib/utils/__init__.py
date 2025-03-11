import ast
import collections
import contextlib
import ctypes
import functools
import inspect
import struct
import threading
import pathlib
import time
import typing

_T = typing.TypeVar('_T')
_T2 = typing.TypeVar('_T2')


def count_func_time(func):
    import time

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        return func(*args, **kwargs), time.perf_counter() - start

    return wrapper


def num_arr_to_bytes(arr):
    return bytes(arr).split(b'\0', 1)[0]


def is_iterable(v):
    try:
        iter(v)
    except TypeError:
        return False
    else:
        return True


class Counter:
    def __init__(self, start=0):
        self.count = start - 1
        self.lock = threading.Lock()

    def get(self):
        with self.lock:
            self.count += 1
            return self.count


def iter_rm(p: pathlib.Path):
    if p.exists():
        if p.is_file():
            p.unlink()
        else:
            for f in p.iterdir():
                iter_rm(f)
            p.rmdir()


def safe(func: typing.Callable[[...], _T], *args, _handle=BaseException, _default: _T2 = None, **kwargs) -> _T | _T2:
    try:
        return func(*args, **kwargs)
    except _handle:
        return _default


def safe_lazy(func: typing.Callable[[...], _T], *args, _handle=BaseException, _default: _T2 = None,
              **kwargs) -> _T | _T2:
    try:
        return func(*args, **kwargs)
    except _handle:
        return _default(*args, **kwargs)


time_units = [
    (1e-13, "Sv"),
    (1e-12, "ps"),
    (1e-9, "ns"),
    (1e-6, "μs"),
    (1e-3, "ms"),
    (1, "s"),
    (60, "min"),
    (60 * 60, "hour"),
    (60 * 60 * 24, "day"),
    (60 * 60 * 24 * 7, "week"),
]


def fmt_sec(sec: float):
    size, name = 1e-13, "Sv"
    for _size, _name in time_units:
        if sec < _size:
            return f'{sec / size:.3f}{name}'
        size = _size
        name = _name
    return f'{sec / size:.3f}{name}'


def test_time(func, cb=None):
    if cb is None: return lambda _func: test_time(_func, func)

    @functools.wraps(func)
    def foo(*args, **kwargs):
        start = time.perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            cb(func, args, kwargs, time.perf_counter() - start)

    return foo


def extend_list(l: list, size: int, el=None):
    if (s := len(l)) < size:
        l.extend(el for _ in range(size - s))


def dict_find_key(d: dict, val, strict=False):
    try:
        if strict:
            return next(k for k, v in d.items() if v == val)
        else:
            return next(k for k, v in d.items() if v is val)
    except StopIteration:
        raise ValueError(val)


def try_run(try_count, exception_type=Exception, exc_cb=None):
    def dec(func):
        def wrapper(*args, **kwargs):
            _try_count = try_count
            while _try_count > 0:
                try:
                    return func(*args, **kwargs)
                except exception_type as e:
                    if _try_count <= 1:
                        raise e
                    _try_count -= 1
                    if exc_cb:
                        exc_cb(e)

        return wrapper

    return dec


def wait_until(func, timeout=-1, interval=0.1, *args, **kwargs):
    start = time.perf_counter()
    while not func(*args, **kwargs):
        if 0 < timeout < time.perf_counter() - start:
            raise TimeoutError
        time.sleep(interval)


def named_tuple_by_struct(t: typing.Type[_T], s: struct.Struct, buffer: bytearray | memoryview | bytes,
                          offset: int = 0) -> _T:
    return t._make(s.unpack_from(buffer, offset))


def dataclass_by_struct(t: typing.Type[_T], s: struct.Struct, buffer: bytearray | memoryview | bytes,
                        offset: int = 0) -> _T:
    return t(*s.unpack_from(buffer, offset))


def wrap_error(cb, exc_type=Exception, default_rtn=None):
    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exc_type as e:
                cb(e, *args, **kwargs)
                return default_rtn

        return wrapper

    return dec


mv_from_mem = ctypes.pythonapi.PyMemoryView_FromMemory
mv_from_mem.argtypes = (ctypes.c_void_p, ctypes.c_ssize_t, ctypes.c_int)
mv_from_mem.restype = ctypes.py_object


def callable_arg_count(func):
    return len(inspect.signature(func).parameters)


class LRU(collections.OrderedDict[_T, _T2]):
    def __init__(self, *args, _maxsize=128, _getter: typing.Callable[[_T], _T2] = None, _validate: typing.Callable[[_T, _T2], bool] = None, _threadsafe=False, **kwds):
        self.__maxsize = _maxsize
        self.__validate = _validate
        self.__getter = _getter
        self.__lock = (threading.Lock if _threadsafe else contextlib.nullcontext)()
        super().__init__(*args, **kwds)

    def __missing__(self, key):
        if self.__getter:
            self.__setitem(key, value := self.__getter(key))
            return value
        raise KeyError(key)

    def __validate__(self, key, value):
        if self.__validate:
            return self.__validate(key, value)
        return True

    def __call__(self, key):
        return self.__getitem__(key)

    def __getitem__(self, key) -> _T2:
        with self.__lock:
            value = super().__getitem__(key)
            if self.__validate__(key, value):
                self.move_to_end(key)
                return value
            else:
                del self[key]
                value = self.__missing__(key)
                self.__setitem(key, value)
                return value

    @property
    def maxsize(self):
        return self.__maxsize

    @maxsize.setter
    def maxsize(self, value):
        with self.__lock:
            if value < self.__maxsize:
                for k, _ in list(zip(self.keys(), range(value))):
                    del self[k]
            self.__maxsize = value

    @property
    def thread_safe(self):
        return not isinstance(self.__lock, contextlib.nullcontext)

    @thread_safe.setter
    def thread_safe(self, value):
        value = bool(value)
        if value != self.thread_safe:
            self.__lock = (threading.Lock if value else contextlib.nullcontext)()

    def __setitem(self, key, value):
        super().__setitem__(key, value)
        if len(self) > self.__maxsize:
            oldest = next(iter(self))
            del self[oldest]

    def __setitem__(self, key, value):
        with self.__lock:
            self.__setitem(key, value)


def exec_ret(script, globals=None, locals=None, *, filename="<string>"):
    '''Execute a script and return the value of the last expression'''
    stmts = list(ast.iter_child_nodes(ast.parse(script)))
    if not stmts:
        return None
    if isinstance(stmts[-1], ast.Expr):
        # the last one is an expression and we will try to return the results
        # so we first execute the previous statements
        if len(stmts) > 1:
            exec(compile(ast.Module(body=stmts[:-1]), filename=filename, mode="exec"), globals, locals)
        # then we eval the last one
        return eval(compile(ast.Expression(body=stmts[-1].value), filename=filename, mode="eval"), globals, locals)
    else:
        # otherwise we just execute the entire code
        return exec(compile(script, filename=filename, mode='exec'), globals, locals)


def repeat_add(start, times, step=1):
    for _ in range(times):
        yield start
        start = start + step


def iter_repeat_add(d, add=0):
    start, times, step = d
    if isinstance(start, int):
        for i in range(times):
            yield start + add
            add += step
    else:
        for i in range(times):
            yield iter_repeat_add(start, add)
            add += step


def seq_dif(seq):
    if len(seq) < 2:
        raise ValueError()
    _n = next(it := iter(seq))
    dif = (n := next(it)) - _n
    while 1:
        try:
            if (_n := next(it)) - n != dif:
                raise ValueError()
        except StopIteration:
            return dif
        n = _n


def seq_to_repeat_add(seq):
    return seq[0], len(seq), seq_dif(seq)


def seq_to_range(seq):
    if (dif := seq_dif(seq)) == 0:
        raise ValueError()
    return seq[0], seq[-1] + (1 if dif > 0 else -1), dif
