import requests
import threading
import queue

url = ""
threads = 25
q = queue.Queue()

for i in range(threads):
    q.put(1)


def post():
    global url
    while not q.empty():
        q.get()
        resp = requests.post(url, data={'money': 1})
        print(resp.text)


if __name__ == "__main__":
    for i in range(threads):
        t = threading.Thread(target=post)
        t.start()

    for i in range(threads):
        t.join()
