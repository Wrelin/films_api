import asyncio
import time


async def main():
    # sync_hello()
    tasks = [
        asyncio.create_task(async_hello()),
        asyncio.create_task(async_hello()),
    ]
    await asyncio.gather(*tasks)


def sync_hello():
    print('Hello')
    time.sleep(3)
    print('world')


async def async_hello():
    print('Hello')
    await asyncio.sleep(3)
    print('world')


if __name__ == '__main__':
    asyncio.run(main())
