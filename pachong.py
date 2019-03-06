import requests
import json

class Spider(object):
    def start_request(self):
        for i in range(0,100,20):
            response = requests.get('URL')
            data = json.loads(response.content.decode())['data']
            self.data_xpath(data)


    def data_xpath(self, data):
        dt_list = data['rl']
        for dt in dt_list:
            src = 
