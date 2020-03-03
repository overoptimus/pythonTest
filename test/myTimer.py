import time as t

class MyTimer():
    def __init__(self):
        self.begin = 0
        self.end = 0
        self.prompt = '未开始计时...'

    def start(self):
        self.begin = t.time()
        self.prompt = '请先停止计时'
        print('计时开始...')

    def stop(self):
        if not self.begin:
            return '请先开始计时...'
        else:
            self.end = t.time()
            self._calc()
            print('计时结束...')

    def _calc(self):
        self.prompt = '总共用时' + str(self.end - self.begin) + '秒'

    def __str__(self):
        return self.prompt

    def __repr__(self):
        return self.prompt
