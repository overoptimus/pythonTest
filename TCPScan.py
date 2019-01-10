import optparse
from socket import *

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost,tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        print('[+] %d/tcp open' %tgtPort)
        print('[+] ' + str(results))
        connSkt.close()
    except:
        print('[-] %d/tcp closed' %tgtPort)


def portScan(tgtHost, tgtPorts):
    try:
        tgtIp = gethostbyname(tgtHost)
    except:
        print("[-] Connot resolve '%s': Unknown host" %tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIp)
        print('\n[+] Scan Results for: ' + tgtName[0])
    except:
        print('\n[+] Scan Results for: ' + tgtIp)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print('Scanning port ' + tgtPort)
        connScan(tgtHost, int(tgtPort))


def main():
    parse = optparse.OptionParser('usage %prog -H' + ' <target host> -p <target port>')
    parse.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parse.add_option('-p', dest='tgtPort', type='int', help='specify target port')
    (options, args) = parse.parse_args()
    tgtHost = options.tgtHost
    tgtPost = options.tgtPort

if (tgtHost == None) | (tgtPort == None):
    print(parse.usage)
    exit(0)
