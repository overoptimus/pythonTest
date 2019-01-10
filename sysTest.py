import sys
import os
if len(sys.argv) == 2:
    fileName = sys.argv[1]
    if not os.path.isfile(fileName):
        print('[-] ' + fileName + ' does not exist.')
        exit(0)
    if not os.access(file,os.R_OK):
        print('[-] ' + fileName + ' access denied.')
        exit(0)
    print('[+] Reading vulnerabilities From: ' + fileName)
