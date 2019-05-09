# -*- coding: utf-8 -*-

import requests
import bs4
import re

def open_url(url):
    proxies = {
        'http': '127.0.0.1:1080',
        'https': '127.0.0.1:1080'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)


    return res

def find_movies(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    movies = []
    targets = soup.find_all('div', class_='hd')
    for each in targets:
        movies.append(each.a.span.text)

    ranks = []
    targets = soup.find_all('span', class_='rating_num')
    for each in targets:
        ranks.append(each.text)

    result = []
    length = len(movies)
    for i in range(length):
        result.append(movies[i] + ' ' + ranks[i])
    return result

def find_depth(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    page = soup.find('span', class_='next').previous_sibling.previous_sibling.text
    return int(page)

def main():
    host = 'https://movie.douban.com/top250'
    res = open_url(host)
    page = find_depth(res)
    for i in range(page):
        url = 'https://movie.douban.com/top250?start={}&filter='.format(i * 25)
        res = open_url(url)
        result = find_movies(res)
        with open('豆瓣top250.txt', 'w', encoding='UTF-8') as f:
            for each in result:
                print(each)
                f.write(each + '\n')

if __name__ == '__main__':
    main()
