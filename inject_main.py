# -*- coding: utf-8 -*-
import os
import os
import sys
import base64
import requests
import wmi
import json
import tkinter as tk
from nylib.hook import create_hook
from nylib.winutils import enable_privilege
from nylib.process import Process
from gui.guicopy import start_gui
import time

import sys
import time
import os
from nylib.winutils.process import enable_privilege,run_admin
from nylib.winutils.python_loader import run_script
from nylib.process import Process


def main():
    
    enable_privilege()
    print('Hello, world!')
    print('sys.executable:', sys.executable)
    print('os.getcwd():', os.getcwd())
    os.system("cls")
    print('''

███████╗██╗   ██╗ ██████╗██╗  ██╗    ███████╗███████╗██╗  ██╗██╗██╗   ██╗
██╔════╝██║   ██║██╔════╝██║ ██╔╝    ██╔════╝██╔════╝╚██╗██╔╝██║██║   ██║
█████╗  ██║   ██║██║     █████╔╝     █████╗  █████╗   ╚███╔╝ ██║██║   ██║
██╔══╝  ██║   ██║██║     ██╔═██╗     ██╔══╝  ██╔══╝   ██╔██╗ ██║╚██╗ ██╔╝
██║     ╚██████╔╝╚██████╗██║  ██╗    ██║     ██║     ██╔╝ ██╗██║ ╚████╔╝ 
╚═╝      ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═══╝   

 ██████╗ ██████╗ ███████╗███████╗███╗   ██╗██████╗ ██╗      █████╗ ██╗   ██╗███████╗██████╗ 
██╔════╝ ██╔══██╗██╔════╝██╔════╝████╗  ██║██╔══██╗██║     ██╔══██╗╚██╗ ██╔╝██╔════╝██╔══██╗
██║  ███╗██████╔╝█████╗  █████╗  ██╔██╗ ██║██████╔╝██║     ███████║ ╚████╔╝ █████╗  ██████╔╝
██║   ██║██╔══██╗██╔══╝  ██╔══╝  ██║╚██╗██║██╔═══╝ ██║     ██╔══██║  ╚██╔╝  ██╔══╝  ██╔══██╗
╚██████╔╝██║  ██║███████╗███████╗██║ ╚████║██║     ███████╗██║  ██║   ██║   ███████╗██║  ██║
 ╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═══╝╚═╝     ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
                                                                                                                        
ACT 不算开？卫月不算开？哟呵，那些个自诩只开不影响游戏平衡的插件的绿色玩家
还有号称只捣鼓游戏模组的黄色玩家，可真是太 “可爱” 啦！您瞧瞧，他们一边大义凛然地宣称自己的所作所为毫无不妥
一边堂而皇之地利用着这些所谓 “不影响平衡” 的东西，在游戏里横冲直撞，这脸皮厚度，简直比城墙拐弯还厚呐。
要是真不影响平衡，咋不见他们在公平竞技的纯原生游戏环境里，靠着真本事打出一片天呢？
每次被质疑了，就拿 “插件和模组无害” 当挡箭牌，糊弄谁呢？真是搞笑了。

''')
    jfiejfpwjfepwofjewpofj = True
    if jfiejfpwjfepwofjewpofj is True:
        try:
            start_gui()
        except Exception as e:
            print("Imgui Error occurred -", e)     




res = main()
