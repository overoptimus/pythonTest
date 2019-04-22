import urllib.request as r
import re, os

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

def get_img():
    url = 'https://tieba.baidu.com/p/3385100879'
    html = get_response(url).decode('UTF-8')
    p = r'<img class="BDE_Image" src="([^"]+\.jpg)"'
    img_list = re.findall(p, html)
    save_imgs(img_list)


def save_imgs(img_list):
    os.mkdir('tieba')
    os.chdir('tieba')
    for img_url in img_list:
        # a = img_url.find('src="') + 5
        # b = img_url.find('"', a)
        # img_url = img_url[a:b]

        print(img_url)
        file_name = img_url.split('/')[-1]
        # with open(file_name, 'wb') as f:
        #     f.write(get_response(img_url))
        r.urlretrieve(img_url, filename=file_name, reporthook=None, data=None)

if __name__ == '__main__':
    get_img()
