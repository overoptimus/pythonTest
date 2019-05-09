import requests
import json
def open_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        'referer': 'https://music.163.com/song?id={}'.format(1362247767)
    }
    data = {
        'params': 'qLfsjKA18O7j+TjkCR3Ffhhr8gHyDrqB3sVbvbeABmUGQpvyWIm4EfDnPPJsQb7hw/7w50SZW2JDUD+m4xLQaDKnwsYcSULTfFl38EHEA2KLZaQECd+g+DkOWZn17x1RDCviJQ0iuVY+oVXB4cWzoRRvXxW/rHbducsUIGKnh+PYZVQndcHGyKc+QTqkFfTi',
        'encSecKey': '6f979dfba8058c14f6b878561740a8faed910aac44b41a7909b1009897dcdbdfb6871637273ed3ab4b135e28f36c1f67bd734f6d3e1d167a30bdbf21fdcb9331e363cd8a902eb3802ca3b1361226cf6ad4ea1c261922b283e056a8b02e1574b968087f53be0bdc479da80fa3e3142f56cffb2470140c1c319780032cf6132b83'
    }
    res = requests.post(url, data=data, headers=headers)
    return res

def main():
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(1362247767)
    res = open_url(url)
    res = json.loads(res.text)
    # print(res['hotComments'][0]['content'])
    comments = res['hotComments']

    with open('wangyiyun.txt', mode='w', encoding='utf-8') as f:
        for comment in comments:
            f.write(str(comments.index(comment)) + '\n' + comment['content'] + '\n')

if __name__ == '__main__':
    main()
