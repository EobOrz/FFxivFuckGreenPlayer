import ctypes
from ctypes import wintypes

from . import structure

dll = ctypes.WinDLL('dwmapi.dll')

HRESULT = ctypes.c_long

DwmExtendFrameIntoClientArea = dll.DwmExtendFrameIntoClientArea
DwmExtendFrameIntoClientArea.restype = HRESULT
DwmExtendFrameIntoClientArea.argtypes = (
    wintypes.HWND,  # hWnd
    ctypes.POINTER(structure.Margins),  # pMarInset
)
