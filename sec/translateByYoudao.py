import urllib.request as r
import urllib.parse as p
import json
import time

while True:
    content = input('请输入要翻译的句子(输入‘q！退出’):')
    if content == 'q!' or content =='q！':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
    }

    data = {
        'i': content,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15556331144091',
        'sign': '7bab40c97c5ba63ba688626b17f9dbfd',
        'ts': '1555633114409',
        'bv': '94d71a52069585850d26a662e1bcef22',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    data = p.urlencode(data).encode('UTF-8')
    # print(type(data))
    req = r.Request(url, data=data, headers=headers)

    response = r.urlopen(req)
    html = response.read().decode('UTF-8')
    html = json.loads(html)
    # print(type(html))
    print(html['translateResult'][0][0]['tgt'])
    time.sleep(2)
