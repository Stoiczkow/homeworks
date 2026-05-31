import asyncio
import time

async def wait(t):
    await asyncio.sleep(t)

async def main():
    time_start = time.time()
    waiting_list = [asyncio.sleep(x) for x in [1, 4, 2]]

    corutines = asyncio.gather(*waiting_list)
    await corutines
    time_finished = time.time() - time_start
    print(time_finished)

asyncio.run(main())