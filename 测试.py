# coding=UTF-8

import socket

host = 'https://www.baidu.com'

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM,)
except Exception as e:
    print(e, '创建套接字失败')


remote_ip = socket.gethostbyname(host)
print(remote_ip)
