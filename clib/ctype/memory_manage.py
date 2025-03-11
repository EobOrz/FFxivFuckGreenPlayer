import bisect
import io


class ChunkManager:
    def __init__(self, ptr, size):
        self.ptr = ptr
        self.size = size
        init_chunk = (0, size)  # (offset, size)

        self.chunks_by_offset = [init_chunk]
        self.chunks_by_size = [init_chunk]

        self.allocated = {}  # (offset, size)[]

    def can_allocate(self, size):
        size = 8 if size <= 8 else ((size + 0xf) & ~0xf)
        return size if self.chunks_by_size and size <= self.chunks_by_size[-1][1] else 0

    def alloc(self, size):
        if not (size := self.can_allocate(size)): return None
        offset, chunk_size = self.chunks_by_size.pop(bisect.bisect_left(self.chunks_by_size, size, key=lambda x: x[1]))
        self.chunks_by_offset.pop(bisect.bisect_left(self.chunks_by_offset, offset, key=lambda x: x[0]))
        self.allocated[offset] = size
        if size < chunk_size:
            new_off = offset + size
            new_size = chunk_size - size
            item = (offset + size, chunk_size - size)
            self.chunks_by_offset.insert(bisect.bisect_left(self.chunks_by_offset, new_off, key=lambda x: x[0]), item)
            self.chunks_by_size.insert(bisect.bisect_left(self.chunks_by_size, new_size, key=lambda x: x[1]), item)
        return self.ptr + offset

    def free(self, ptr):
        offset = ptr - self.ptr
        if offset not in self.allocated: return False
        size = self.allocated.pop(offset)

        i = bisect.bisect_left(self.chunks_by_offset, offset, key=lambda x: x[0])

        if i < len(self.chunks_by_offset):
            _offset, _size = self.chunks_by_offset[i]
            if offset + size == _offset:
                self.chunks_by_offset.pop(i)
                self.chunks_by_size.pop(bisect.bisect_left(self.chunks_by_size, _size, key=lambda x: x[1]))
                size += _size

        if i > 0:
            _offset, _size = self.chunks_by_offset[i - 1]
            if _offset + _size == offset:
                i -= 1
                self.chunks_by_offset.pop(i)
                self.chunks_by_size.pop(bisect.bisect_left(self.chunks_by_size, _size, key=lambda x: x[1]))
                offset = _offset
                size += _size

        item = (offset, size)
        self.chunks_by_offset.insert(i, item)
        self.chunks_by_size.insert(bisect.bisect_left(self.chunks_by_size, size, key=lambda x: x[1]), item)

        return True

    def fmt_chunks(self):
        s = io.StringIO()
        s.write(f'=== {len(self.chunks_by_offset)} chunks ===')
        for i, (offset, size) in enumerate(self.chunks_by_offset):
            s.write(f'\n[{i}] {self.ptr + offset:04x} - {self.ptr + offset + size:04x} ({size:04x})')
        return s.getvalue()


class MemoryManager:
    def __init__(self, alloc, free):
        self._alloc = alloc
        self._free = free
        self.chunks = []

    def __del__(self):
        for cm in self.chunks:
            self._free(cm.ptr)

    def create_chunk(self, size):
        size = (size + 0xfffff) & ~0xfffff
        ptr = self._alloc(size)
        cm = ChunkManager(ptr, size)
        i = bisect.bisect_left(self.chunks, ptr, key=lambda x: x.ptr)
        self.chunks.insert(i, cm)
        return cm

    def alloc(self, size):
        cm = next((cm for cm in self.chunks if cm.can_allocate(size)), None) or self.create_chunk(size)
        return cm.alloc(size)

    def free(self, ptr):
        i = bisect.bisect_left(self.chunks, ptr, key=lambda x: x.ptr)
        if i < 0: return False
        return self.chunks[i - 1].free(ptr)

    def fmt_chunks(self):
        s = io.StringIO()
        cnt = 0
        for cm in self.chunks:
            for i, (offset, size) in enumerate(cm.chunks_by_offset):
                s.write(f'\n[{cnt}] {cm.ptr + offset:04x} - {cm.ptr + offset + size:04x} ({size:04x})')
                cnt += 1
        return f"=== {cnt} chunks ===" + s.getvalue()


def test_chunk():
    from nylib.process import Process
    cm = MemoryManager(Process.current.alloc, Process.current.free)
    # cm = ChunkManager(0x100000, 0x1000)

    a1 = cm.alloc(0x10)
    print(f"{a1=:x}")
    a2 = cm.alloc(0x20)
    print(f"{a2=:x}")
    a3 = cm.alloc(0x30)
    print(f"{a3=:x}")
    a4 = cm.alloc(0x30)
    print(f"{a4=:x}")

    print(cm.fmt_chunks())
    assert cm.free(a1)
    print(cm.fmt_chunks())
    assert cm.free(a3)
    print(cm.fmt_chunks())
    assert cm.free(a2)
    print(cm.fmt_chunks())
    assert cm.free(a4)
    print(cm.fmt_chunks())


if __name__ == '__main__':
    test_chunk()
    test_chunk()
