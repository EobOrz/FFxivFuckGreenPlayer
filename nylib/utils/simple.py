import functools
import threading

aligned4 = lambda v: (v + 0x3) & (~0x3)
aligned8 = lambda v: (v + 0x7) & (~0x7)
aligned16 = lambda v: (v + 0xf) & (~0xf)


class Counter:
    def __init__(self, start=0):
        self.value = start
        self.lock = threading.Lock()

    def get(self):
        with self.lock:
            self.value += 1
            return self.value


def clean_cached_property(instance):
    for k in dir(instance.__class__):
        v = getattr(instance.__class__, k)
        if isinstance(v, functools.cached_property):
            instance.__dict__.pop(k, None)
