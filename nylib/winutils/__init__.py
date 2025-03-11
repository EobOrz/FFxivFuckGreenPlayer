from .process import *
from .. import winapi


def write_to_clipboard(text: str):
    text = text.encode('utf-16le') + b'\0\0'
    if not winapi.OpenClipboard(0):
        raise ctypes.WinError()
    winapi.EmptyClipboard()
    try:
        if not (h := winapi.GlobalAlloc(0x0042, len(text))):
            raise ctypes.WinError()
        if not (p := winapi.GlobalLock(h)):
            raise ctypes.WinError()
        winapi.memcpy(p, text, len(text))
        winapi.GlobalUnlock(h)
        winapi.SetClipboardData(13, h)
        return True
    finally:
        winapi.CloseClipboard()
