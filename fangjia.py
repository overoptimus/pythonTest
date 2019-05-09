import requests
import bs4
import re, openpyxl

def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
    }
    proxies = {
        'http': '127.0.0.1:1080',
        'https': '127.0.0.1:1080'
    }
    # res = requests.get(url, headers=headers, proxies=proxies)
    res = requests.get(url, headers=headers)


    return res

def get_fangjia(res):
    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    data = []
    targets = soup.find('div', id='Cnt-Main-Article-QQ')
    targets = targets.find_all('p', style='TEXT-INDENT: 2em')
    targets = iter(targets)
    for i in targets:
        if i.text.isnumeric():
            data.append([
                re.search(r'\[(.*)\]', next(targets).text).group(1),
                re.search(r'\d.*', next(targets).text).group(),
                re.search(r'\d.*', next(targets).text).group(),
                re.search(r'\d.*', next(targets).text).group()

                # next(targets).text,
                # next(targets).text,
                # next(targets).text,
                # next(targets).text
            ])
    return data

def to_excl(data):
    wb = openpyxl.Workbook()
    wb.guess_types = True
    ws = wb.active
    ws.append(['城市', '平均房价', '平均工资', '房价工资比'])
    for each in data:
        ws.append(each)

    wb.save('2017年中国主要城市房价工资比排行表.xlsx')

def main():
    url = 'https://news.house.qq.com/a/20170702/003985.htm'
    res = open_url(url)
    data = get_fangjia(res)
    to_excl(data)
    
if __name__ == '__main__':
    main()
