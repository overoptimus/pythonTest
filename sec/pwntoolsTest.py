'''
@Description: 
@Version: 2.0
@Author: 0pt1mus
@Date: 2020-05-02 00:38:10
@LastEditors: 0pt1mus
@LastEditTime: 2020-05-06 17:50:49
'''
from pwn import *

shellcode = shellcraft.amd64.sh()
print(binascii.b2a_hex(asm(shellcode, arch='amd64' )))