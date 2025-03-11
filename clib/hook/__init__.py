import ctypes
import typing
from . import detours


class Hook:

    def __init__(self, at: int, hook_func, restype: typing.Type = ctypes.c_void_p, argtypes: typing.Iterable[typing.Type] = ()):
        """
        创建一个 hook， 注意需要手动调用 install()

        :param at: 该函数的内存地址
        :param hook_func: 钩子函数
        :param restype: 返回类型
        :param argtypes: 参数类型（列表）
        """

        self.at = at
        self.interface = ctypes.CFUNCTYPE(restype, *argtypes)
        self._hook_function = self.interface(lambda *args: hook_func(self, *args))
        self.original = self.interface(at)
        self.is_installed = False

    def install(self):
        if not self.is_installed:
            with detours.DetourTransaction():
                detours.DetourAttach(ctypes.byref(self.original), self._hook_function)
            self.is_installed = True
        return self

    def uninstall(self):
        if self.is_installed:
            with detours.DetourTransaction():
                detours.DetourDetach(ctypes.byref(self.original), self._hook_function)
            self.is_installed = False
        return self

    def __call__(self, *args):
        self.interface(self.at)(*args)


def create_hook(at: int, restype: typing.Type = ctypes.c_void_p, argtypes: typing.Iterable[typing.Type] = (), auto_install=False):
    """
    使用装饰器创建一个 hook， 注意需要调用 install()

    :param at: 该函数的内存地址
    :param restype: 返回类型
    :param argtypes: 参数类型（列表）
    :param auto_install: 是否自动调用 install
    :return:
    """
    if auto_install:
        return lambda func: Hook(at, func, restype, argtypes).install()
    else:
        return lambda func: Hook(at, func, restype, argtypes)


def test():
    import ctypes.wintypes
    t_dll = ctypes.CDLL('User32.dll')

    MessageBoxW = ctypes.CFUNCTYPE(ctypes.wintypes.INT, ctypes.wintypes.HWND, ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR, ctypes.wintypes.UINT)(t_dll.MessageBoxW)

    @create_hook(at=ctypes.cast(MessageBoxW, ctypes.c_void_p).value, restype=ctypes.wintypes.INT, argtypes=[ctypes.wintypes.HWND, ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR, ctypes.wintypes.UINT], auto_install=True)
    def message_box_hook(_hook, handle, title, message, flag):
        res = _hook.original(handle, "hooked " + title, "hooked " + message, flag)
        print(f"hooked: {title} - {message}, return {res}")
        return res

    MessageBoxW(None, 'hi content!', 'hi title!', 0)

    message_box_hook.uninstall()

    MessageBoxW(None, 'hi content!', 'hi title!', 0)
