import os
import sys
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# 现在可以安全地进行绝对导入
from nylib.hook import create_hook
from nylib.process import Process
from nylib.winutils import enable_privilege
from pynput import keyboard
from .utils import LocalPlayer
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
    def __init__(self,local_player):
        self.inject = False
        self.move_casting = False
        self.p = Process.current
        self.local_player = local_player
        try:
            self.execute_base = self.p.base_static_scanner().find_address("48 89 5C 24 ?? 48 89 74 24 ?? 4C 89 64 24 ?? 55 41 56 41 57 48 8B EC 48 83 EC 70")
            self.updatepositioninstance = self.p.read_u16(self.p.base_static_scanner().find_address("41 B8 ?? ?? ?? ?? F6 C2") + 0x2)
            self.updatepositionhandler = self.p.read_u16(self.p.base_static_scanner().find_address("48 89 5C 24 ?? 48 89 74 24 ?? 57 48 81 EC ?? ?? ?? ?? 48 8B 05 ?? ?? ?? ?? 48 33 C4 48 89 84 24 ?? ?? ?? ?? 48 8B F9 41 8B D8") + 0x51)

            print(f"SendPacket Path: Succeed | MovePacketOpcode {self.updatepositioninstance}|{self.updatepositionhandler}")
        except Exception as e:
            self.execute_base = None
            self.updatepositioninstance = None
            self.updatepositionhandler = None    
            print("SendPacket Path: error")  
            print(e)  
        if self.execute_base is not None:
            self._create_hook()   

    def _create_hook(self):
        self.hook = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.execute_base, restype=ctypes.c_byte, argtypes=[ctypes.c_int64, ctypes.c_int64, ctypes.c_int64, ctypes.c_byte])
        def hook(hook, a1, a2, a3, a4):

            opcode = ctypes.cast(a2, ctypes.POINTER(ctypes.c_ushort)).contents.value
            if self.local_player.execute_base != 0 and self.move_casting:
                if self.p.read_u16(self.local_player.is_casting) != 0:
                    if opcode == self.updatepositioninstance or opcode == self.updatepositionhandler:
                        return 1
            print(f"来源:{a1} | 操作码:{opcode} | {a3} | {a4}")
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
            if self.inject is True:
                imgui.Text("  ")
                imgui.SameLine()
                change, new_val_1 = imgui.Checkbox("CastingMoveable", self.move_casting)
                if change: 
                    self.move_casting = new_val_1     

        else:imgui.Text("SendPacket: error")