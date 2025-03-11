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

class CommandHookConfig(ctypes.Structure):
    _fields_ = [
        ('prefix', ctypes.c_char * 0x10),
    ]

class CommandObserver:
    def update(self, args):
        raise NotImplementedError("Subclasses must implement this method")
    
class Commander():
    def __init__(self):
        self.inject = False
        self.cfg = CommandHookConfig()
        self.p = Process.current
        self.observers = []
        try:
            self.execute_base = self.p.base_static_scanner().find_address("40 ? 53 57 41 ? 41 ? 41 ? 48 ? ? ? ? 48 ? ? ? ? ? ? 48 ? ? ? ? ? ? 48 ? ? 48 89 45 ? 65")
            print("Commander Path: Succeed")
        except:
            self.execute_base = None
            print("Commander Path: error")  
        if self.execute_base is not None:
            self._create_hook()   

    def register_observer(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def _create_hook(self):
        self.hook = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.execute_base, restype=ctypes.c_void_p, argtypes=[ctypes.c_int64, ctypes.c_int, ctypes.c_int64, ctypes.POINTER(ctypes.c_char_p), ctypes.c_int64], auto_install=True)
        def hook(hook, a1, a2, a3, cmd_ptr, a5):
            inp = cmd_ptr[0]
            parts = inp.split()
            args = [part.decode('utf-8') for part in parts]
            self.notify_observers(args)
            return hook.original(a1, a2, a3, cmd_ptr, a5)
        return hook

    def notify_observers(self, args):
        for observer in self.observers:
            observer.update(args)






class Campeng:
    def __init__(self):
        self.inject = False
        self.p = Process.current
        # cn self.execute_base = self.p.base_static_scanner().find_address("e8 ? ? ? ? 45 ? ? ? 84 ? 0f 84 ? ? ? ? f3 ? ? ? ? ?")
        try:
            self.execute_base = self.p.base_static_scanner().find_address("45 ? ? ? 8b ? f3 ? ? ? ? f3 ? ? ? ? ? ? ? ? 48 ? ?")
            print("CamNoCollision Path: Succeed")
        except:
            self.execute_base = None
            print("CamNoCollision Path: error")
        if self.execute_base is not None:
            self.address = self.execute_base
            self.original_bytes = self._read_original_bytes()
            self.patched_bytes = b'\x30\xc0\x90\x90\x90'

    def _read_original_bytes(self):
        original_bytes = []
        for i in range(5):
            original_bytes.append(self.p.read_u8(self.address + i))
        return bytes(original_bytes)

    def apply_patch(self):
        for i, byte in enumerate(self.patched_bytes):
            self.p.write_u8(self.address + i, byte)

    def restore_patch(self):
        for i, byte in enumerate(self.original_bytes):
            self.p.write_u8(self.address + i, byte)

    def hook_func(self):
        self.apply_patch()

    def unhook_func(self):
        self.restore_patch()

    def draw_panel(self):
        if self.execute_base is not None:
            changed, new_val = imgui.Checkbox("CamNoCollision", self.inject)
            if changed:
                self.inject = new_val
                if self.inject:
                    print('Hook Install CamNoCollision')
                    self.hook_func()
                else:
                    print('Hook Uninstall CamNoCollision')
                    self.unhook_func()
        else:
            imgui.Text("CamNoCollision Path: error")



class FallCheckPatch:
    def __init__(self):
        self.inject = False
        self.p = Process.current    
        self.hook_message = "None" 
        try:
            self.address = self.p.base_static_scanner().find_val("e8 * * * * 8b ? 85 ? 0f 88 ? ? ? ? 48 ? ? ? f3 ? ? ? ? ? ? ?")[0]
            print("FallCheckPatch Path: Succeed")
        except:
            self.address = None
            print("FallCheckPatch Path: error")  
        if self.address is not None:
            self._create_hook()
    def _create_hook(self):
        self.fall_hook = self._create_hook_func()




    def _create_hook_func(self):
        @create_hook(at=self.address, restype= ctypes.c_int64, argtypes=[ctypes.c_int64,ctypes.c_int64,ctypes.c_int64])
        def hook(hook, a1,a2,a3):
            self.hook_message = f'{a1} + {a2} + {a3}'
            res = -1#hook.original(a1,a2,a3)
            return res
        return hook


    def draw_panel(self):
        if self.address is not None:
            changed, new_val = imgui.Checkbox("FallCheckPatch", self.inject)
            if changed:
                self.inject = new_val
                if self.inject:
                    print('Hook Install FallCheckPatch')
                    self.fall_hook.install()                    
                else:
                    print('Hook Uninstall FallCheckPatch')
                    self.fall_hook.uninstall() 
            imgui.Text(self.hook_message)
        else:
            imgui.Text("FallCheckPatch Path: error")


class NoRender:
    def __init__(self):
        self.inject = False
        self.p = Process.current
        self.listener = None 
        self.no_render_control = False        
        # cn self.execute_base = self.p.base_static_scanner().find_address("e8 ? ? ? ? 45 ? ? ? 84 ? 0f 84 ? ? ? ? f3 ? ? ? ? ?")
        try:
            self.execute_base = self.p.base_static_scanner().find_address("e8 ? ? ? ? 80 7b ? ? 74 ? 48 ? ? 48 ? ? ff 50 ? 84")
            print("NoRender Path: Succeed")
        except:
            self.execute_base = None
            print("NoRender Path: error")
        if self.execute_base is not None:
            self.start_listener()            
            self.address = self.execute_base
            self.original_bytes = self._read_original_bytes2()#b'\xe8\x04\x22\x2c\x00'
            self.patched_bytes = b'\x90\x90\x90\x90\x90'

    def start_listener(self):
        # 定义回调函数
        def on_press(key):
            if key == keyboard.Key.f1:
                if self.inject is True:
                    if self.no_render_control is False:
                        self.hook_func()
                        print('Hook Install NoRender')
                        self.no_render_control = True

        # 启动监听器
        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def _read_original_bytes2(self):
        original_bytes = (self.p.read_u8(self.address),
                        self.p.read_u8(self.address + 1),
                        self.p.read_u8(self.address + 2),
                        self.p.read_u8(self.address + 3),
                        self.p.read_u8(self.address + 4)) 
        return bytes(original_bytes)

    def apply_patch(self):
        for i, byte in enumerate(self.patched_bytes):
            self.p.write_u8(self.address + i, byte)

    def restore_patch(self):
        for i, byte in enumerate(self.original_bytes):
            self.p.write_u8(self.address + i, byte)

    def hook_func(self):
        self.apply_patch()

    def unhook_func(self):
        self.restore_patch()

    def draw_panel(self):
        if self.execute_base is not None:
            changed, new_val = imgui.Checkbox("NoRender(Danger)", self.inject)
            if imgui.IsItemHovered():
                imgui.BeginTooltip()
                imgui.Text("It will freeze your game screen, but game events are running")
                imgui.EndTooltip()            
            if changed:
                self.inject = new_val
            if self.inject is True:
                imgui.Text('F1 on')
        else:
            imgui.Text("NoRender Path: error")