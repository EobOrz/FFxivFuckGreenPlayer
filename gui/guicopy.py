import os
import sys
import threading
import traceback
import contextlib
from pynput import keyboard
from nylib.winutils.pipe_rpc import RpcServer
from .hacks import GrandCompany,ShopQuantity,MovePermission,AntiKnock,GetActionRange,NoBackswing,Speed
from .hacks import PassWall,ExecuteCommand,AnimLock,NoActionMove
from .utils import Campeng,FallCheckPatch,NoRender
import pathlib


color_themes = ["Dark", "Light", "Classic"]
color_theme_index = 2 
selected_tab = "Home"
should_show_window = True


grand_company = GrandCompany()
shop_quantity = ShopQuantity()
move_permission = MovePermission()
anti_knock = AntiKnock()
action_range = GetActionRange()
no_backswing = NoBackswing()
speed = Speed()
pass_wall = PassWall()
execute_command = ExecuteCommand()
anim_lock = AnimLock()
campeng = Campeng()
fall_check = FallCheckPatch()
no_render = NoRender()
no_action_move = NoActionMove()
def main():

    from nylib.hook import create_hook
    from nylib.process import Process
    import ctypes.wintypes
    if ctypes.windll.kernel32.GetModuleHandleW('d3d11.dll'):
        mode = "Dx11"
    elif ctypes.windll.kernel32.GetModuleHandleW('d3d12.dll'):
        mode = "Dx12"
    else:
        mode = None

    import pyimgui
    import pyimgui.imgui as imgui
    import pyimgui.imgui.ctx as imgui_ctx
    from pyimgui import Dx11Inbound, Dx12Inbound     

    wnd = None
    last_io = None

    @create_hook(
        at=Process.current.get_proc_address('User32.dll', 'SetCursor'),
        restype=ctypes.wintypes.BOOL, argtypes=[ctypes.wintypes.HANDLE]
    )
    def set_cursor_hook(_hook, handle):
        if not wnd.isInLogic and getattr(last_io, 'WantCaptureMouse', False): return False
        return _hook.original(handle)

    @create_hook(
        at=Process.current.get_proc_address('User32.dll', 'SetCursorPos'),
        restype=ctypes.wintypes.BOOL, argtypes=[ctypes.wintypes.INT, ctypes.wintypes.INT]
    )
    def set_cursor_pos_hook(_hook, x, y):
        if not wnd.isInLogic and getattr(last_io, 'WantCaptureMouse', False):
            return True
        return _hook.original(x, y)
    

    def on_press(key):
        global should_show_window
        try:
            if key == keyboard.Key.insert:
                should_show_window = not should_show_window
        except AttributeError:
            print("Exception in on_press: ", traceback.format_exc())

    # 启动 pynput 键盘监听的线程
    def start_listener():
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()
    
    
    
    listener_thread = threading.Thread(target=start_listener)
    listener_thread.daemon = True
    listener_thread.start()

    datas = {
        'test_string': 'Hello, world!',
    }

    def init_func():
        io = imgui.GetIO()
        io.IniFilename = None
        io.ConfigFlags = io.ConfigFlags & ~ imgui.ImGuiConfigFlags_ViewportsEnable  # disable multi-window                
        font_dir = pathlib.Path(os.environ['WINDIR']) / 'fonts'
        if (font_file := font_dir / 'msyh.ttc').is_file():
            datas['font'] = io.Fonts.AddFontFromFileTTF(str(font_file), 20, None, io.Fonts.GetGlyphRangesChineseFull())
            io.Fonts.Build()
            wnd.InvalidateDeviceObjects()
        datas['is_init'] = True



    def draw_func():
        global selected_tab
        
        nonlocal last_io
        last_io = imgui.GetIO()
        #imgui.GetIO().IniFilename = None
        if not datas.get('is_init', False):
            wnd.CallBeforeFrameOnce(init_func)
        try:
            set_cursor_pos_hook.wantCaptureMouse = imgui.GetIO().WantCaptureMouse
        except Exception as e:
            traceback.print_exc()
           
        try:
            display = imgui.GetIO().DisplaySize
            #imgui.SetWindowSize(imgui.ImVec2(400, 600))
            imgui.SetWindowPos(imgui.ImVec2(50, 50))
            # 开始渲染窗口
            with imgui_ctx.PushFont(im_font) if (im_font := datas.get('font')) else contextlib.nullcontext():
                if should_show_window:
                    imgui.PushStyleVar(imgui.ImGuiStyleVar_Alpha, 1.0)  # Tab transparency
                    imgui.PushStyleVar(imgui.ImGuiStyleVar_WindowRounding, 4.0)  # Rounding of framesFrame
                    imgui.PushStyleVar(imgui.ImGuiStyleVar_FrameRounding, 4.0)
                    if imgui_ctx.Begin("FUCK GreenPlayer",flags=imgui.ImGuiWindowFlags_NoResize):
                        if imgui.BeginChild("Sidebar", imgui.ImVec2(200, 400), True):
                            imgui.PushStyleColor(imgui.ImGuiCol_Button, imgui.ImVec4(0.0, 0.0, 0.0, 0.0))  # RGBA
                            imgui.PushStyleColor(imgui.ImGuiCol_ButtonHovered, imgui.ImVec4(0.4, 0.4, 0.9, 1.0))
                            imgui.PushStyleColor(imgui.ImGuiCol_ButtonActive, imgui.ImVec4(0.5, 0.5, 0.9, 1.0))  
                            #imgui.PushStyleColor(7,imgui.ImVec4(0.9, 0.1, 0.1, 0.0))  # 按钮颜色
                            #imgui.PushStyleColor(8,imgui.ImVec4(0.9, 0.1, 0.1, 0.7))  # 按钮悬停颜色
                            #imgui.PushStyleColor(9,imgui.ImVec4(0.7, 0.0, 0.0, 1.0))  # 按钮按下颜色

                            # 按钮逻辑
                            highlight_panel = selected_tab == "MoveHack"
                            if highlight_panel:
                                imgui.PushStyleColor(imgui.ImGuiCol_Button, imgui.ImVec4(0.4, 0.4, 0.9, 1.0))                                
                            if imgui.Button("MoveHack", imgui.ImVec2(180, 40)):
                                selected_tab = "MoveHack"
                            if highlight_panel:
                                imgui.PopStyleColor(1)           

                            highlight_panel2 = selected_tab == "FunctionHack"
                            if highlight_panel2:
                                imgui.PushStyleColor(imgui.ImGuiCol_Button, imgui.ImVec4(0.4, 0.4, 0.9, 1.0))   
                            if imgui.Button("FunctionHack", imgui.ImVec2(180, 40)):
                                selected_tab = "FunctionHack"
                            if highlight_panel2:
                                imgui.PopStyleColor(1)  

                            highlight_panel3 = selected_tab == "CombatHack"
                            if highlight_panel3:
                                imgui.PushStyleColor(imgui.ImGuiCol_Button, imgui.ImVec4(0.4, 0.4, 0.9, 1.0))  
                            if imgui.Button("CombatHack", imgui.ImVec2(180, 40)):
                                selected_tab = "CombatHack"
                            if highlight_panel3:
                                imgui.PopStyleColor(1)  

                            highlight_panel4 = selected_tab == "DevTools"
                            if highlight_panel4:
                                imgui.PushStyleColor(imgui.ImGuiCol_Button, imgui.ImVec4(0.4, 0.4, 0.9, 1.0))  
                            if imgui.Button("DevTools", imgui.ImVec2(180, 40)):
                                selected_tab = "DevTools"
                            if highlight_panel4:
                                imgui.PopStyleColor(1)                                  
                            # 弹出样式
                            imgui.PopStyleColor(3)

                        imgui.EndChild()

                        # 内容区域
                        imgui.SameLine()
                        if imgui.BeginChild("Content", imgui.ImVec2(500, 400), True):
                            if selected_tab == "MoveHack":
                                move_permission.draw_panel()
                                anti_knock.draw_panel()
                                speed.draw_panel()
                                pass_wall.draw_panel()
                                fall_check.draw_panel()                                
                            elif selected_tab == "FunctionHack":
                                grand_company.draw_panel()
                                shop_quantity.draw_panel()
                                campeng.draw_panel()
                            elif selected_tab == "CombatHack":
                                action_range.draw_panel()     
                                no_backswing.draw_panel()  
                                no_action_move.draw_panel()
                            elif selected_tab == "DevTools":
                                execute_command.draw_panel() 
                                anim_lock.draw_panel()
                                no_render.draw_panel()
                        imgui.EndChild()

                    # 结束窗口
                    imgui.End()
                    imgui.PopStyleVar(3)
        except Exception as e:
            print(e)

    if mode == 'Dx11':
        wnd = Dx11Inbound(draw_func)
    elif mode == 'Dx12':
        wnd = Dx12Inbound(draw_func)
    else:
        raise RuntimeError('No supported graphics API found.')
    threading.Timer(1, lambda: (
        wnd.Attach(),
        set_cursor_hook.install(),
        set_cursor_pos_hook.install(),
        print('install_imgui done')
    )).start()


    def run_script(path):
        with open(path, 'r') as f:
            code = compile(f.read(), path, 'exec')
            exec(code, namespace := {'__file__': path})
        return namespace.get('res')

    RpcServer(rf'\\.\\pipe\\NyPipe-pid-{os.getpid()}', {
        'run_script': run_script,
    }).serve()


def start_gui():
    main()