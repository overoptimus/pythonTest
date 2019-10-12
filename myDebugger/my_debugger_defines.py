from ctypes import *

# 为ctype变量创建符合匈牙利命名风格的匿名，这样使代码更接近Win32的风格
WORD = c_ushort
DWORD = c_ulong
LPBYTE = POINTER(c_ubyte)
LPTSTR = POINTER(c_char)
HANDLE = c_void_p

# 常值定义
DEBUG_PROCESS = 0x00000001
CREATE_NEW_CONSOLE = 0x00000010

# 定义函数CreateProcessA()所需要的结构体


class STARTUPINFO(Structure):
    __fields__ = [
        ("cb", DWORD),
        ("IpReserved", LPTSTR),
        ("IpDesktop", LPTSTR),
        ("IpTitle", LPTSTR),
        ("dwX", DWORD),
        ("dwY", DWORD),
        ("dwXSize", DWORD),
        ("dwYSize", DWORD),
        ("dwXCountChars", DWORD),
        ("dwYCountChars", DWORD,
        ("dwFillAttribute", DWORD),
        ("dwFlags", DWORD),
        ("wShowWindow", WORD),
        ("cbReserved2", WORD),
        ("IpReserved2", LPBYTE),
        ("hStdInput", HANDLE),
        ("hStdOutput", HANDLE),
        ("hStdError", HANDLE),
    ]


class PROCESS_INFORMATION(Structure):
    __fields__=[
        ("hProcess", HANDLE),
        ("hThread", HANDLE),
        ("dwProcessId", DWORD),
        ("dwThreadId", DWORD),
    ]
