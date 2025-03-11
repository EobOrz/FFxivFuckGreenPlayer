# from https://gist.github.com/wontoncc/1808234

import win32api
import win32gui
import win32con

def find_name(val):
    return [k for k, v in win32con.__dict__.items() if v == val]

class WindowsBalloonTip:
    def __init__(self, title, msg, icon_path: str = None):
        # Register the Window class.
        wc = win32gui.WNDCLASS()
        hinst = wc.hInstance = win32api.GetModuleHandle(None)
        wc.lpszClassName = "PyTaskbar"
        wc.lpfnWndProc = {
            win32con.WM_DESTROY: self.OnDestroy,
        }
        classAtom = win32gui.RegisterClass(wc)
        # Create the Window.
        # style = win32con.WS_OVERLAPPED | win32con.WS_SYSMENU
        style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        self.hwnd = win32gui.CreateWindow(classAtom, "Taskbar", style, 0, 0, win32con.CW_USEDEFAULT, win32con.CW_USEDEFAULT, 0, 0, hinst, None)
        win32gui.UpdateWindow(self.hwnd)
        icon_flags = win32con.LR_LOADFROMFILE | win32con.LR_DEFAULTSIZE
        try:
            hicon = win32gui.LoadImage(hinst, icon_path, win32con.IMAGE_ICON, 0, 0, icon_flags)
        except:
            hicon = win32gui.LoadIcon(0, win32con.IDI_APPLICATION)
        flags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
        nid = (self.hwnd, 0, flags, win32con.WM_USER + 20, hicon, "tooltip")
        win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)
        win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY, (self.hwnd, 0, win32gui.NIF_INFO, win32con.WM_USER + 20, hicon, "Balloon  tooltip", title, 200, msg))

    def close(self):
        win32gui.DestroyWindow(self.hwnd)

    def OnDestroy(self, hwnd, msg, wparam, lparam):
        nid = (self.hwnd, 0)
        win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)
        win32api.PostQuitMessage(0)

