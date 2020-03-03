import requests
import re, json

def open_url(keyword):
    payload = {
        'q': keyword,
        'sort': 'sale-desc'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }
    url = 'https://s.taobao.com/search'
    res = requests.get(url, headers=headers, params=payload)

    return res


def main():
    keyword = input('请输入搜索关键字：')
    res = open_url(keyword)
    with open('taobao.txt', mode='w', encoding='utf-8') as f:
        f.write(res.text)

if __name__ == '__main__':
    main()
