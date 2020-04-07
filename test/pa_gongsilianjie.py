import requests
from bs4 import BeautifulSoup


def get_urls():
    url_list = []
    with open('./urls.txt', 'r') as f:
        urls = f.readlines()
        for url in urls:
            url_list.append(url.strip())

    return url_list


def get_html(url):
    req = requests.get(url)
    req.coding = 'utf-8'
    return req.text


def get_target(html):
    soup = BeautifulSoup(html, 'html.parser')
    tds = soup.find_all(
        'td', attrs={'align': 'left', 'valign': 'top', 'class': 'xycpl_sh22 lf15'})
    # for i in range(len(tds)):
    #     print(i, tds[i])
    with open('./shebei.txt', 'a') as f:
        f.write('http://oa.zycg.cn/' + tds[0].find_all('a')[0]['href'] + '\n')


def main():
    url_list = get_urls()
    for url in url_list:
        html = get_html(url)
        get_target(html)


if __name__ == '__main__':
    main()
