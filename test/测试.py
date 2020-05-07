'''
@Description: 
@Version: 2.0
@Author: 0pt1mus
@Date: 2020-03-03 22:47:06
@LastEditors: 0pt1mus
@LastEditTime: 2020-05-07 16:09:13
'''
# coding=UTF-8

import socket

host = 'https://www.baidu.com'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
except Exception as e:
    print(e, '创建套接字失败')


remote_ip = socket.gethostbyname(host)
print(remote_ip)
