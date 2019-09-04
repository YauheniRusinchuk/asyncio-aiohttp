import asyncio
import aiohttp
from time import time


def write_img(data):
    filename = f'file.{int(time() * 1000)}.jpeg'
    with open(filename, 'wb') as file:
        file.write(data)


async def fetch(url, session):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        write_img(data)

async def start():
    url:str  = 'https://loremflickr.com/320/240'
    tasks:list = []
    async with aiohttp.ClientSession() as session:
        for i in range(10):
            task = asyncio.create_task(fetch(url, session))
            tasks.append(task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(start())
