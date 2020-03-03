import time
import asyncio
from aiohttp import ClientSession

# async def hello():
#     asyncio.sleep(1, result=None, loop=None)
#     print('hello world: %s' %time.time())
#
# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())
#
# loop = asyncio.get_event_loop()
#
# if __name__ == '__main__':
#     run()

# def hello():
#     time.sleep(1)
#     print('hello world: %s' %time.time())
#
# def run():
#     for i in range(5):
#         hello()
#
#
# if __name__ == '__main__':
#     run()

url = 'https://www.baidu.com/{}'

async def hello(url):
    async with ClientSession() as session:
        async with session.get(url) as response:
            status = response.status()
            print(status)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello(url))
