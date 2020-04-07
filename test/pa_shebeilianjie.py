import requests
from bs4 import BeautifulSoup

url = 'http://oa.zycg.cn/td_xxlcpxygh/platform'

req = requests.get(url)
req.encoding = 'utf-8'

soup = BeautifulSoup(req.text, 'html.parser')
# print(soup.prettify())
tds = soup.find_all('td', attrs={'class': 'grade3',
                                 'valign': 'top', 'align': 'left'})

a_s = tds[11].find_all('a')
with open('./urls.txt', 'w') as f:
    for a in a_s:
        f.write('http://oa.zycg.cn/' + a['href'] + '\n')
# a = a.find('a')
# print(a)
