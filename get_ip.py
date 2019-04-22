import urllib.request as r
import re

def get_response(url):
    # proxys = ['117.191.11.71:8080', '117.191.11.102:8080', '117.191.11.108:80']
    # proxy_support = r.ProxyHandler({'http': random.choice(proxys)})
    # opener = r.build_opener(proxy_support)
    # r.install_opener(opener)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    req = r.Request(url, headers=headers)

    html = r.urlopen(req).read()
    # print(url)
    return html

def get_ip():
    url = 'https://www.kuaidaili.com/free/'
    html = get_response(url).decode('UTF-8')
    p = r'(?:(?:25[0-5]|2[0-4]\d|[0-1]?\d?\d)\.){3}(?:25[0-5]|2[0-4]\d|[0,1]?\d?\d)'
    ip_list = re.findall(p, html)
    for ip in ip_list:
        print(ip)


if __name__ == '__main__':
    get_ip()
