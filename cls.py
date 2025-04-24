import os
import sys as system

def clear():
    if system.platform.startswith(('win32')):
        cmd = "cls"
    elif system.platform.startswith(('linux', 'cygwin', 'darwin', 'freebsd')):
        cmd = "clear && printf '\e[3J'"
    else:
        print("Platform not recognised")
        cmd = input("Clear screen command on your computer")
        if cmd == Null or cmd == "":
            print('\n'*250)
    if cmd != Null:
        cmd_cls_v = os.system(cmd)
        del cmd_cls_v
# With modifications of Desadena and code of Catafrancia123
