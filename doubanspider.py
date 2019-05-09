import urllib.request as r
import requests
import bs4
import re


headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
j = 0
for i in range(50):
    url = 'https://movie.douban.com/top250?start={}&filter='.format(j)
    req = r.Request(url, headers=headers)

    response = r.urlopen(req)
    html = response.read().decode('UTF-8')
    p = '<span class="title">(.*)</span>'
    nameList = re.findall(p, html)
    for name in nameList:
        name = name.strip('&nbsp;/&nbsp;')
        print(name)
    j += 25
