import zipfile
import optparse
from threading import Thread

def extractFile(zFile,password):
    try:
        zFile.extractall(pwd=password)
        print('[+] Found password ' + password + '\n')
    except:
        pass


def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()



zFile = zipfile.ZipFile('evil.zip')
try:
    zFile.extractall(pwd="ecret")
except Exception as e:
    print(e)
