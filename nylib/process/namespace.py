import typing

if typing.TYPE_CHECKING:
    from . import Process

_aligned4 = lambda v: (v + 0x3) & (~0x3)
_aligned16 = lambda v: (v + 0xf) & (~0xf)


class Namespace:
    chunk_size = 0x10000

    def __init__(self, process: 'Process'):
        self.process = process
        self.res = []
        self.ptr = 0
        self.remain = 0
        self._protection = 0x40  # PAGE_EXECUTE_READWRITE

    @property
    def protection(self):
        return self._protection

    @protection.setter
    def protection(self, v):
        self._protection = v
        for alloc_addr, alloc_size in self.res:
            self.process.virtual_protect(alloc_addr, alloc_size, v)

    def store(self, data: bytes):
        self.process.write(p_buf := self.take(len(data)), data)
        return p_buf

    def take(self, size):
        size = _aligned16(size)
        if self.remain < size:
            alloc_size = max(self.chunk_size, size)
            alloc_addr = self.process.alloc(alloc_size)
            self.res.append((alloc_addr, alloc_size))
            self.process.virtual_protect(alloc_addr, alloc_size, self.protection)
            self.remain = alloc_size - size
            self.ptr = alloc_addr + size
            return alloc_addr
        else:
            self.remain -= size
            res = self.ptr
            self.ptr += size
            return res

    def free(self):
        while self.res:
            self.process.free(*self.res.pop())

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.free()
