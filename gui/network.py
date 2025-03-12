import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# 现在可以安全地进行绝对导入
from nylib.hook import create_hook
from nylib.process import Process
from nylib.winutils import enable_privilege
from pynput import keyboard
import pyimgui
import pyimgui.imgui as imgui
import pyimgui.imgui.ctx as imgui_ctx
import ctypes
import sys

#发包
#SendPacket = "48 89 5C 24 ?? 48 89 74 24 ?? 4C 89 64 24 ?? 55 41 56 41 57 48 8B EC 48 83 EC 70"
#移动读条Opode定位
#UpdatePositionInstance = (("41 B8 ?? ?? ?? ?? F6 C2") + 0x2)
#UpdatePositionHandler = (("48 89 5C 24 ?? 48 89 74 24 ?? 57 48 81 EC ?? ?? ?? ?? 48 8B 05 ?? ?? ?? ?? 48 33 C4 48 89 84 24 ?? ?? ?? ?? 48 8B F9 41 8B D8") + 0x51)


class SendPacket():
    def __init__(self):
        self.inject = False
        self.p = Process.current
        try:
            self.execute_base = self.p.base_static_scanner().find_address("48 89 5C 24 ?? 48 89 74 24 ?? 4C 89 64 24 ?? 55 41 56 41 57 48 8B EC 48 83 EC 70")
            print("SendPacket Path: Succeed")
        except:
            self.execute_base = None
            print("SendPacket Path: error")  
        if self.execute_base is not None:
            self._create_hook()   

    def _create_hook(self):
        self.hook = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.execute_base, restype=ctypes.c_byte, argtypes=[ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_byte])
        def hook(hook, a1, a2, a3, a4):
            print(f"{a1} | {a2} | {a3} | {a4}")
            return hook.original(a1, a2, a3, a4)
        return hook

    def draw_panel(self):
        if self.execute_base is not None:      
            changed, new_val = imgui.Checkbox("SendPacket", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install SendPacket')
                    self.hook.install()
                if self.inject is False:
                    print('Hook uninstall SendPacket')
                    self.hook.uninstall()
        else:imgui.Text("SendPacket: error")