import urllib.request as r
import random

url = 'https://www.whatismyip.com/my-ip-information/?iref=home  '

ipList = ['117.191.11.71:8080', '117.191.11.102:8080', '117.191.11.108:80']

proxy_support = r.ProxyHandler({'http': random.choice(ipList)})

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
# }

opener = r.build_opener(proxy_support)
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36')]
r.install_opener(opener)

req = r.Request(url)

response = r.urlopen(req)
html = response.read()
html = html.decode('UTF-8')
a = html.find('ip')
print(html[a:a+300])
