import ctypes

from .detours import *


def check(c):
    if c: raise ctypes.WinError(c)


class DetourTransaction:
    def __init__(self, set_thread=None):
        self.set_thread = set_thread

    def __enter__(self):
        check(DetourTransactionBegin())
        try:
            check(DetourUpdateThread(self.set_thread or ctypes.windll.kernel32.GetCurrentThread()))
        except:
            check(DetourTransactionAbort())
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            check(DetourTransactionCommit())
        else:
            check(DetourTransactionAbort())
            return False
