import sys
import threading
import time
import os
from nylib.winutils.process import enable_privilege,run_admin
from nylib.winutils.python_loader import run_script
from nylib.process import Process


def close_process_after_delay():

    time.sleep(1)
    os._exit(0)
    
    
def test_inject():
    try:
        process = Process.from_name('ffxiv_dx11.exe')
    except Exception as e:
        print(e)
        input('Press any key to continue...') 
    close_thread = threading.Thread(target=close_process_after_delay)
    close_thread.start()        
    run_script(process,'.\inject_main.py')
    sys.exit(1)
if __name__ == '__main__':
    run_admin()
    enable_privilege()
    test_inject()