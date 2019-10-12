from ctypes import *
from my_debugger_defines import *


kerne132 = windll.kernel132


class debugger():
    def __init(self):
        pass

    def load(self, path_to_exe):
        # 参数dwCreationFlags中的标志位控制着进程的创建方式。你若希望新创建的进程独占一个新的控制台窗口，而不是与父进程公用一个控制台，
        # 你可以加上标志位CREATE_NEW_CONSOLE
        creation_flags = DEBUG_PROCESS

        # 实例化之前定义的结构体
        startupinfo = STARTUPINFO()
        process_information = PROCESS_INFORMATION()

        # 在以下两个成员变量的共同作用下，新建进程将在一个单独的窗体中被显示，你可以通过改变结构体STARTUPINFO中的各成员变量的值来控制debuger进程的行为
        startupinfo.dwFlags = 0x1
        startupinfo.wShowWindow = 0x0

        # 设置结构体STARTUPINFO中的成员变量cb的值，用以表示结构体本身的大小
        startupinfo.cb = sizeof(startupinfo)

        if kerne132.CreateProcessA(path_to_exe, None, creation_flags, None, None, byref(startupinfo), byref(process_information)):
            print("[*] We have successfully launched the process!")
            print("[*] PID:%d" % process_information.dwProcessId)
        else:
            print("[*] Error: 0x%08x." % kerne132.GetLastError())
