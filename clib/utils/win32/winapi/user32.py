import ctypes
from ctypes import wintypes

from . import structure

dll = ctypes.WinDLL('user32.dll')

GetClientRect = dll.GetClientRect
GetClientRect.restype = wintypes.BOOL
GetClientRect.argtypes = (
    wintypes.HWND,  # hWnd
    ctypes.POINTER(structure.RECT),  # lpRect
)

GetWindowRect = dll.GetWindowRect
GetWindowRect.restype = wintypes.BOOL
GetWindowRect.argtypes = (
    wintypes.HWND,  # hWnd
    ctypes.POINTER(structure.RECT),  # lpRect
)

SetActiveWindow = dll.SetActiveWindow
SetActiveWindow.restype = wintypes.HWND
SetActiveWindow.argtypes = (
    wintypes.HWND,  # hWnd
)

GetDC = dll.GetDC
GetDC.restype = wintypes.HDC
GetDC.argtypes = (
    wintypes.HWND,  # hWnd
)

GetDesktopWindow = dll.GetDesktopWindow
GetDesktopWindow.restype = wintypes.HWND
GetDesktopWindow.argtypes = ()

GetDeviceCaps = dll.GetDeviceCaps
GetDeviceCaps.restype = ctypes.c_int
GetDeviceCaps.argtypes = (
    wintypes.HDC,  # hdc
    ctypes.c_int,  # nIndex
)

SetLayeredWindowAttributes = dll.SetLayeredWindowAttributes
SetLayeredWindowAttributes.restype = wintypes.BOOL
SetLayeredWindowAttributes.argtypes = (
    wintypes.HWND,  # hwnd
    wintypes.COLORREF,  # crKey
    ctypes.c_byte,  # bAlpha
    wintypes.DWORD,  # dwFlags
)

SetWindowLong = dll.SetWindowLongW
SetWindowLong.restype = wintypes.LONG
SetWindowLong.argtypes = (
    wintypes.HWND,  # hWnd
    ctypes.c_int,  # nIndex
    wintypes.LONG,  # dwNewLong
)

GetWindowText = dll.GetWindowTextW
GetWindowText.restype = ctypes.c_int
GetWindowText.argtypes = (
    wintypes.HWND,  # hWnd
    ctypes.c_wchar_p,  # lpString
    ctypes.c_int,  # nMaxCount
)

mouse_event = dll.mouse_event
mouse_event.restype = ctypes.c_void_p
mouse_event.argtypes = (
    wintypes.DWORD,  # dwFlags
    wintypes.DWORD,  # dx
    wintypes.DWORD,  # dy
    wintypes.DWORD,  # dwData
    ctypes.c_void_p,  # dwExtraInfo
)

EnumWindows = dll.EnumWindows
EnumWindows.restype = wintypes.BOOL
EnumWindows.argtypes = (
    ctypes.c_void_p,  # lpEnumFunc
    wintypes.LPARAM,  # lParam
)

FindWindow = dll.FindWindowW
FindWindow.restype = wintypes.HWND
FindWindow.argtypes = (
    ctypes.c_wchar_p,  # lpClassName
    ctypes.c_wchar_p,  # lpWindowName
)

SetWindowPos = dll.SetWindowPos
SetWindowPos.restype = wintypes.BOOL
SetWindowPos.argtypes = (
    wintypes.HWND,  # hWnd
    wintypes.HWND,  # hWndInsertAfter
    ctypes.c_int,  # X
    ctypes.c_int,  # Y
    ctypes.c_int,  # cx
    ctypes.c_int,  # cy
    wintypes.UINT,  # uFlags
)

GetAsyncKeyState = dll.GetAsyncKeyState
GetAsyncKeyState.restype = ctypes.c_short
GetAsyncKeyState.argtypes = (
    ctypes.c_int,  # vKey
)
