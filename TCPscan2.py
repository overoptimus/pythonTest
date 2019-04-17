from socket import *

class Tcpscan():
    def __init__(self, host, ports):
        self.host = host
        self.ports = ports

    def startscan(self):
        for port in self.ports:
            try:
                s = socket(family=AF_INET, type=SOCK_STREAM)
                s.connect((host, port))
                print('[+] %d open' %(port))
                s.close()
            except:
                pass
                # print('[-] %d close' %(port))


if __name__ == '__main__':
    scan = Tcpscan('192.168.107.129', range(1, 65536))
    scan.startscan()
