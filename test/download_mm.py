import urllib.request as r
import os
import random

def get_response(url):
    proxys = ['117.191.11.71:8080', '117.191.11.102:8080', '117.191.11.108:80']
    proxy_support = r.ProxyHandler({'http': random.choice(proxys)})
    opener = r.build_opener(proxy_support)
    r.install_opener(opener)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    req = r.Request(url, headers=headers)

    html = r.urlopen(req).read()
    print(url)
    return html

def get_page(url):
    html = get_response(url).decode('UTF-8')
    a = html.find('current-comment-page') + 23
    b = html.find(']', a)

    return html[a:b]

def find_imgs(page_url):
    html = get_response(page_url).decode('UTF-8')
    img_addrs = []

    a = html.find('img src=')
    while a != -1:
        b = html.find('.jpg', a, a+255)
        if b != -1:
            # print(html[a:b+4])
            img_addrs.append('http:' + html[a+9:b+4])
        else:
            b = a + 9
        a = html.find('img src=', b)
    # print(img_addrs)
    return img_addrs

def save_imgs(folder, img_addrs):
    for each in img_addrs:
        img_name = each.split('/')[-1]
        with open(img_name, mode='wb') as img_file:
            html = get_response(each)
            img_file.write(html)

def download_mm(folder = 'OOXX', pages = 10):
    if not os.path.exists(os.getcwd() + '/' + folder):
        os.mkdir(folder)
    os.chdir(folder)

    url = 'http://jandan.net/ooxx/'
    page_num = int(get_page(url)) + 1

    for i in range(pages):
        page_num -= 1
        page_url = url + 'page-' + str(page_num) + '#comments'
        # print(page_url)
        img_addrs = find_imgs(page_url)
        save_imgs(folder, img_addrs)


if __name__ == '__main__':
    download_mm()
