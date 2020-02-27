from subprocess import Popen, PIPE

from socket import *
from time import ctime

HOST = 'localhost'  # 本机作为服务端，地址可以不填写
PORT = 21567  # 端口
BUFSIZE = 1024  # 传输数据所占大小

ADDR = (HOST, PORT)

# 服务端代码
tcpServer = socket(AF_INET, SOCK_STREAM)
# 地址绑定套接字
tcpServer.bind(ADDR)
# 服务端监听
tcpServer.listen(5)

# 接听数据
while True:
    print('waiting for connection...')
    # 绑定
    tcpClient, addr = tcpServer.accept()
    print('..connected from:', addr)
    while True:
        data = tcpClient.recv(BUFSIZE)
        if not data:
            break
        cmd = Popen(['/bin/bash', '-c', data], stdin=PIPE, stdout=PIPE)
        data = cmd.stdout.read()
        data = f'[{ctime()}] {data.decode()}'
        data = data.encode()
        tcpClient.send(data)

# 关闭连接
tcpClient.close()
tcpServer.close()
