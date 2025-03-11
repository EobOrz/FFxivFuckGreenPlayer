from clib.hook import create_hook
from clib.process import Process
from clib.winutils import enable_privilege
from .utils import Commander,CommandObserver

import ctypes
import pyimgui
import pyimgui.imgui as imgui
import pyimgui.imgui.ctx as imgui_ctx
commander = Commander() 

class GrandCompany:
    def __init__(self):
        self.p = Process.current
        self.hook_return_value = 17  # 初始化默认的返回值
        self.max_accel = False
        try:
            self.a = self.p.base_static_scanner().find_address("0F B6 81 ?? ?? ?? ?? FF C8 83 F8 ?? 73")
            print('GrandCompany: Succeed')
        except:
            self.a = None
            print('Error in GrandCompany')
        if self.a is not None:
            self._create_hook()

    def _create_hook(self):
        self.grand_company_hook = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.a, restype=ctypes.c_int64, argtypes=[ctypes.c_int64])
        def hook(hook, a1):
            return self.hook_return_value
        return hook
    

    def draw_panel(self):
        if self.a is not None:      
            changed, new_val = imgui.Checkbox("GrandCompany", self.max_accel)
            if changed: 
                self.max_accel = new_val
                if self.max_accel is True:
                    print('Hook Install GrandCompany')
                    self.grand_company_hook.install()
                if self.max_accel is False:
                    print('Hook uninstall GrandCompany')
                    self.grand_company_hook.uninstall()
        else:imgui.Text("GrandCompany: error")



class ShopQuantity:
    def __init__(self):
        self.p = Process.current
        self.hook_return_value = 999  # 初始化默认的返回值
        self.hook_original_value = 99
        self.max_accel = False
        try:
            #self.a = self.p.base_static_scanner().find_address("41 ?? 63 00 00 00 41 ?? ?? 44 ?? ?? ?? 41")+0x2
            self.a = self.p.base_static_scanner().find_address("49 ? ? ? ? ? ? 4c ? ? ? ? ? ? be ? ? ? ? 90")+0xe +1
            print("ShopQuantity: Succeed")
        except:
            self.a = None
            print('Failed! ShopQuantity invalid! Please notify the administrator to fix it.')


    def draw_panel(self):


        if self.a is not None:      
            changed, new_val = imgui.Checkbox("ShopQuantity", self.max_accel)
            if changed: 
                self.max_accel = new_val
                if self.max_accel is True:
                    print('Write ShopQuantity To 999')
                    self.p.write_u16(self.a,self.hook_return_value)
                if self.max_accel is False:
                    print('Recovery ShopQuantity To 99')
                    self.p.write_u16(self.a,self.hook_original_value)
        else:
            imgui.Text("ShopQuantity: error")



class MovePermission:
    def __init__(self):
        self.inject = False

        self.p = Process.current
        self.commander = commander
        self.commander.register_observer(self)  # 使用 self 来注册 Player 实例 
        try:
            self.p_code, =self.p.base_static_scanner().find_val("e8 * * * * 84 ? 74 ? 48 c7 05")
            print("MovePermission: Succeed")
        except:
            self.p_code = None
            print("MovePermission: error")

        if self.p_code is not None:
            self._create_hook()

    def _create_hook(self):
        self.move_permission = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.p_code, restype=ctypes.c_longlong, argtypes=[ctypes.c_int64,ctypes.c_uint,ctypes.c_int,ctypes.c_int])
        def hook(hook, a1,a2,a3,a4):
            
            #print(f"{a1}\n{a2}\n{a3}\n{a4}")
            p_ids = list(range(96, 100)) + [0x3E9, 0x3EE, 0x3EF, 0x3F0]
            if a2 in p_ids:
                return 1
            return hook.original(a1, a2, a3, a4)
        return hook

    def draw_panel(self):
        if self.p_code is not None:
            changed, new_val = imgui.Checkbox("MovePermission", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install MovePermission')
                    self.move_permission.install()
                if self.inject is False:
                    print('Hook Uninstall MovePermission')
                    self.move_permission.uninstall()
        else:imgui.Text("MovePermission: error")

    def update(self, args):
        if len(args) < 4: return
        if args[0] == "/e" and args[1] == "@hacks" and args[2] == "move.move_permission":
            if args[3] == "On":                
                self.move_permission.install()
                self.inject = True
            elif args[3] == "Off":         
                self.move_permission.uninstall() 
                self.inject = False   


class GetActionRange :#line:521

    def __init__ (self):
        self.inject = False
        self.inject_a = False
        self.add = 2.0
        self.add_a = 2.0
        self.hook_message = "None"
        self.hook_message_a = "None"
        self.p = Process.current
        self.commander = commander
        self.commander.register_observer(self)  # 使用 self 来注册 Player 实例           
        try:
            self.p_code, =self.p.base_static_scanner().find_addresses("48 89 5c 24 ? 57 48 ? ? ? 48 ? ? ? ? ? ? 8b ? 0f 29 74 24 20")#line:546
            print("GetActionRange: Succeed")
        except:
            self.p_code = None
            print("GetActionRange: error")
        try: #40 ? 48 ? ? ? 48 ? ? 80 ? ? 75 ? 48 ? ? ff 50 ?
            self.p_code_a, =self.p.base_static_scanner().find_val("e8 * * * * f3 ? ? ? ? ? ? ? f3 ? ? ? f3 ? ? ? 0f ? ? f3 0f 11 83 ? ? ? ?")#line:546
            #self.p_code_a, =self.p.base_static_scanner().find_val("E8 * * * * F3 0F 58 F0 F3 0F 10 05 ? ? ? ?")#line:546
            print("GetActorRadius: Succeed")
        except:
            self.p_code_a = None
            print("GetActorRadius: error")


        if self.p_code is not None:
            self._create_hook()
        if self.p_code_a is not None:
            self._create_hook_a()


    def _create_hook(self):
        self.get_action_range = self._create_hook_func()
    def _create_hook_a(self):
        self.get_actor_radius = self._create_hook_func_a()

    def _create_hook_func(self):
        @create_hook(at=self.p_code, restype=ctypes.c_float, argtypes=[ctypes.c_uint])
        def hook(hook, a1):
            res = hook.original(a1) + self.add
            self.hook_message = f'{hook.original(a1)} + {self.add}'
            return res
        return hook
    def _create_hook_func_a(self):
        @create_hook(at=self.p_code_a, restype=ctypes.c_float, argtypes=[ctypes.c_uint64, ctypes.c_ubyte])
        def hook(hook, a1 ,a2):
            res = max(hook.original(a1,a2) + self.add_a,0)
            self.hook_message_a = f'{hook.original(a1,a2)} + {self.add_a}'
            return res
        return hook
    
    def draw_panel(self):
        if self.p_code is not None:
            changed, new_val = imgui.Checkbox("GetActionRange", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install GetActionRange')
                    self.get_action_range.install()
                if self.inject is False:
                    print('Hook Uninstall GetActionRange')
                    self.get_action_range.uninstall()
            if self.inject is True:
                #try:
                change,new_val = imgui.SliderFloat('AddRange', self.add, 0, 20, '%.1f')
                if change:self.add = new_val
                if imgui.Button("Restore to 0"):self.add = 0
                imgui.SameLine()
                if imgui.Button("Set to 2"):self.add = 2
                imgui.SameLine()
                if imgui.Button("Set to 5"):self.add = 5 
                imgui.SameLine()
                if imgui.Button("Set to 20"):self.add = 20                     
                imgui.Text(self.hook_message)
        else:imgui.Text("GetActionRange: error")
        if self.p_code_a is not None:
            changed, new_val = imgui.Checkbox("GetActorRadius", self.inject_a)
            if changed: 
                self.inject_a = new_val
                if self.inject_a is True:
                    print('Hook Install GetActorRadius')
                    self.get_actor_radius.install()
                if self.inject_a is False:
                    print('Hook Uninstall GetActorRadius')
                    self.get_actor_radius.uninstall()
            if self.inject_a is True:
                #try:
                change,new_val = imgui.SliderFloat('AddRadius', self.add_a, 0, 5, '%.1f')
                if change:self.add_a = new_val
                if imgui.Button("Restore to 0"):self.add_a = 0
                imgui.SameLine()
                if imgui.Button("Set to 1"):self.add_a = 1                     
                imgui.SameLine()
                if imgui.Button("Set to 2"):self.add_a = 2             
                imgui.Text(self.hook_message_a)
        else:imgui.Text("GetActorRadius: error")
    def update(self, args):
        if len(args) < 4: return
        if args[0] == "/e" and args[1] == "@hacks" and args[2] == "combat.get_action_range":
            if args[3] == "On":                
                self.get_action_range.install()
                self.inject = True
            elif args[3] == "Off":         
                self.add = 0.0
                self.get_action_range.uninstall() 
                self.inject = False   
            else:
                try:
                    # 尝试将 args[3] 转换为浮点数
                    add_value = float(args[3])
                    if add_value >= 0:  # 检查是否为非负数
                        if not self.inject:
                            self.get_action_range.install()
                            self.add = add_value
                            self.inject = True
                        else:
                            self.add = add_value
                except ValueError:
                    print('ValueError')
        elif args[0] == "/e" and args[1] == "@hacks" and args[2] == "combat.get_actor_radius":
            if args[3] == "On":                
                self.get_actor_radius.install()
                self.inject_a = True
            elif args[3] == "Off":         
                self.add_a = 0.0
                self.get_actor_radius.uninstall() 
                self.inject_a = False   
            else:
                try:
                    # 尝试将 args[3] 转换为浮点数
                    add_value = float(args[3])
                    if add_value >= 0:  # 检查是否为非负数
                        if not self.inject_a:
                            self.get_actor_radius.install()
                            self.add_a = add_value
                            self.inject_a = True
                        else:
                            self.add_a = add_value
                except ValueError:
                    print('ValueError')


class AntiKnock:
    def __init__(self):
        self.inject = False
        self.hook_message = "None"
        self.p = Process.current
        self.commander = Commander()
        self.commander.register_observer(self)  # 使用 self 来注册 Player 实例            
        try:
            self.p_code =self.p.base_static_scanner().find_address("48 ? ? 48 89 58 ? 48 89 70 ? 57 48 ? ? ? ? ? ? 0f 29 70 ? 48 ? ? 0f 29 78 ? 44 0f 29 40 ?")
            print("AntiKnock: Succeed")
        except:
            self.p_code = None
            print("AntiKnock: error")

        if self.p_code is not None:
            self._create_hook()


    def _create_hook(self):
        self.anti_knock = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.p_code, restype=ctypes.c_int64, argtypes=[ctypes.c_int64, ctypes.c_float, ctypes.c_float, ctypes.c_int64, ctypes.c_ubyte, ctypes.c_uint])
        def hook(hook, actor_ptr, angle, dis, knock_time, a5, a6):
            res = hook.original(actor_ptr, angle, dis, knock_time, a5, a6)
            if res:
                self.hook_message = f'actor_ptr:{actor_ptr} angle:{angle} dis:{dis} knock_time:{knock_time} a5:{a5} a6:{a6}'
            return hook.original(actor_ptr, 0, 0, 0, a5, a6)
        return hook

    def draw_panel(self):
        if self.p_code is not None:
            changed, new_val = imgui.Checkbox("AntiKnock", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install AntiKnock')
                    self.anti_knock.install()
                if self.inject is False:
                    print('Hook Uninstall AntiKnock')
                    self.anti_knock.uninstall()
            if self.inject is True:
                imgui.Text(self.hook_message)
        else:imgui.Text("AntiKnock: error")

    def update(self, args):
        if len(args) < 4: return
        if args[0] == "/e" and args[1] == "@hacks" and args[2] == "move.anti_knock":
            if args[3] == "On":                
                self.anti_knock.install()
                self.inject = True
            elif args[3] == "Off":         
                self.anti_knock.uninstall() 
                self.inject = False   


class NoBackswing:
    def __init__(self):
        self.inject = False
        self.hook_message = "None"
        self.p = Process.current
        self.commander = commander
        self.commander.register_observer(self)  # 使用 self 来注册 Player 实例          
        try:
            self.p_code =self.p.base_static_scanner().find_val("E8 * * * * C6 83 ? ? ? ? ? E9 96 00 ? ?")[0]
            print("NoBackswing: Succeed")
        except:
            self.p_code = None
            print("NoBackswing: error")
        if self.p_code is not None:
            self._create_hook()


    def _create_hook(self):
        self.no_backswing = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.p_code, restype=ctypes.c_int64, argtypes=[ctypes.c_int64])
        def hook(hook, a1):
            self.hook_message = f"{a1}"
            return a1
        return hook

    def draw_panel(self):
        if self.p_code is not None:
            changed, new_val = imgui.Checkbox("NoBackswing", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install NoBackswing')
                    self.no_backswing.install()
                if self.inject is False:
                    print('Hook Uninstall NoBackswing')
                    self.no_backswing.uninstall()    
            if self.inject is True:
                imgui.Text(self.hook_message)
        else:imgui.Text("NoBackswing: error")

    def update(self, args):
        if len(args) < 4: return
        if args[0] == "/e" and args[1] == "@hacks" and args[2] == "combat.no_back_swing":
            if args[3] == "On":                
                self.no_backswing.install()
                self.inject = True
            elif args[3] == "Off":         
                self.no_backswing.uninstall() 
                self.inject = False   

class Speed:
    def __init__(self):
        self.inject = False
        self.hook_message = "None"
        self.add = 0.0
        self.p = Process.current
        self.commander = commander
        self.commander.register_observer(self)  # 使用 self 来注册 Player 实例  
        try:
            self.p_code =self.p.base_static_scanner().find_address("40 ? 48 ? ? ? 48 ? ? 48 ? ? ? 48 ? ? ff 90 ? ? ? ? 48 ? ? 75 ? f3 ? ? ? ? ? ? ?")
            print("Speed: Succeed")
        except:
            self.p_code = None
            print("Speed: error")
        if self.p_code is not None:
            self._create_hook()


    def _create_hook(self):
        self.speed = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.p_code, restype=ctypes.c_float, argtypes=[ctypes.c_int64])
        def hook(hook, a1):
            res = hook.original(a1) + self.add
            self.hook_message = f'{hook.original(a1)} + {self.add:.2f}'
            return res
        return hook

    def draw_panel(self):
        if self.p_code is not None:
            changed, new_val = imgui.Checkbox("Speed", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install Speed')
                    self.speed.install()
                if self.inject is False:
                    print('Hook Uninstall Speed')
                    self.speed.uninstall()    
            if self.inject is True:

                change,new_val = imgui.SliderFloat('AddSpeed', self.add, 0, 20, '%.2f')
                if change:
                    self.add = new_val
                if imgui.Button("Add 0.1"):
                    self.add += 0.1     
                imgui.SameLine()
                if imgui.Button("Add 0.2"):
                    self.add += 0.2 
                imgui.Text(self.hook_message)
        else:imgui.Text("Speed: error")

    def update(self, args):
        if len(args) < 4: return
        if args[0] == "/e" and args[1] == "@hacks" and args[2] == "move.speed":
            if args[3] == "On":                
                self.speed.install()
                self.inject = True
            elif args[3] == "Off":         
                self.add = 0.0
                self.speed.uninstall() 
                self.inject = False   
            else:
                try:
                    # 尝试将 args[3] 转换为浮点数
                    add_value = float(args[3])
                    if add_value >= 0:  # 检查是否为非负数
                        if not self.inject:
                            self.speed.install()
                            self.add = add_value
                            self.inject = True
                        else:
                            self.add = add_value
                except ValueError:
                    print('ValueError')


class PassWall:
    def __init__(self):
        self.inject = False
        self.p = Process.current
        self.commander = commander
        self.commander.register_observer(self)  # 使用 self 来注册 Player 实例        
        try:
            self.address = self.p.base_static_scanner().find_val("f3 0f 11 44 24 ? 48 ? ? e8 * * * * 44 ? ? ?")[0]
            print("PassWall Path: Succeed")
        except:
            self.address = None
            print("PassWall Path: error")  
        if self.address is not None:
            self.original_bytes = self._read_original_bytes()
            self.patched_bytes = b'\xB0\x00\xC3'

    def _read_original_bytes(self):
        # Read the original 3 bytes from the address
        byte1 = self.p.read_u8(self.address)
        byte2 = self.p.read_u8(self.address + 1)
        byte3 = self.p.read_u8(self.address + 2)
        return bytes([byte1, byte2, byte3])

    def apply_patch(self):
        self.p.write_u8(self.address, self.patched_bytes[0])
        self.p.write_u16(self.address + 1, int.from_bytes(self.patched_bytes[1:], 'little'))

    def restore_patch(self):
        self.p.write_u8(self.address, self.original_bytes[0])
        self.p.write_u16(self.address + 1, int.from_bytes(self.original_bytes[1:], 'little'))

    def hook_func(self):
        self.apply_patch()

    def unhook_func(self):
        self.restore_patch()


    def draw_panel(self):
        if self.address is not None:
            changed, new_val = imgui.Checkbox("PassWall", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install PassWall')
                    self.hook_func()
                if self.inject is False:
                    print('Hook Uninstall PassWall')
                    self.unhook_func()
        else:imgui.Text("PassWall Path: error")

    def update(self, args):
        if len(args) < 4: return
        if args[0] == "/e" and args[1] == "@hacks" and args[2] == "move.pass_wall":
            if args[3] == "On":                
                self.hook_func()
                self.inject = True
            elif args[3] == "Off":                
                self.unhook_func()
                self.inject = False               
  
import ctypes
import glm
import threading
from glm import vec3





class ExecuteCommand:
    def __init__(self):
        self.inject = False
        self.p = Process.current  
        try:
            self.execute_base = self.p.base_static_scanner().find_address("48 89 5C 24 ?? 48 89 6C 24 ?? 48 89 74 24 ?? 57 48 81 EC ?? ?? ?? ?? 48 8B 05 ?? ?? ?? ?? 48 33 C4 48 89 84 24 ?? ?? ?? ?? 8B E9 41 8B D9 48 8B 0D ?? ?? ?? ?? 41 8B F8 8B F2")
            print("ExecuteCommand Path: Succeed")
        except:
            self.execute_base = None
            print("ExecuteCommand Path: error")  
    def draw_panel(self):
        if self.execute_base is not None:
            if imgui.Button("InstantReturn"):
                execute_base_func_ptr = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(self.execute_base)
                execute_base_func_ptr(ctypes.c_int(214), ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0))
            if imgui.IsItemHovered():
                imgui.BeginTooltip()
                imgui.Text("Just like use 'Return'")
                imgui.EndTooltip()
            if imgui.Button("Back To Safearea"):
                execute_base_func_ptr = ctypes.CFUNCTYPE(ctypes.c_void_p, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)(self.execute_base)
                execute_base_func_ptr(ctypes.c_int(213), ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0), ctypes.c_int(0))
            if imgui.IsItemHovered():
                imgui.BeginTooltip()
                imgui.Text("Lalafall is unable to use this feature!")
                imgui.EndTooltip()



class AnimLock:

    def __init__(self):
        self.p = Process.current  # 假设您已经有了当前进程的引用
        try:
            # 使用内存扫描找到特定的指令模式
            self.anim_base = self.p.base_static_scanner().find_val("48 8D 0D * * * * F3 0F 10 13")[0] + 0x08   #anim lock
            self.anim_base1 = self.p.base_static_scanner().find_val("48 8D 0D * * * * F3 0F 10 13")[0] + 0x24  #cast id
            
            print("AnimationLock Address:", hex(self.anim_base))
            print("AnimLock: Succeed")
        except Exception as e:
            print("AnimLock: Error occurred -", e)
            self.anim_base = None

    
    def draw_panel(self):
        #print(f"{self.p.read_float(self.anim_base)}")
        imgui.Text(f"{self.p.read_float(self.anim_base)}")
        imgui.Text(f"{self.p.read_u16(self.anim_base1)}")



class NoActionMove:
    def __init__(self):
        self.inject = False
        self.hook_message = "None"
        self.add = 0.0
        self.p = Process.current
        try:
            self.p_code =self.p.base_static_scanner().find_address("48 89 5C 24 ? 48 89 74 24 ? 57 48 83 EC ? 48 8B F1 0F 29 74 24 ? 48 8B 89 ? ? ? ? 0F 28 F3")
            print("NoActionMove: Succeed")
        except:
            self.p_code = None
            print("NoActionMove: error")
        if self.p_code is not None:
            self._create_hook()


    def _create_hook(self):
        self.no_action_move = self._create_hook_func()

    def _create_hook_func(self):
        @create_hook(at=self.p_code, restype=ctypes.c_uint64, argtypes=[ctypes.c_uint64, ctypes.c_uint8, ctypes.c_uint64, ctypes.c_float, ctypes.POINTER(ctypes.c_uint16)])
        def hook(hook, a1, action_timeline_move_id, target_id, facing, p_action_timeline):
            #timeline = p_action_timeline.contents.value
            block = True
            #for white in self.cfg.action_move_white_list:
            #    if white == 0:
            #        break
            #    if white == timeline:
            #        block = False
            #        break
            #if block:
            return
        return #hook

    def draw_panel(self):
        if self.p_code is not None:
            changed, new_val = imgui.Checkbox("NoActionMove", self.inject)
            if changed: 
                self.inject = new_val
                if self.inject is True:
                    print('Hook Install NoActionMove')
                    self.no_action_move.install()
                if self.inject is False:
                    print('Hook Uninstall NoActionMove')
                    self.no_action_move.uninstall()    
        else:imgui.Text("NoActionMove: error")