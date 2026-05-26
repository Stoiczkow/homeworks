import asyncio
from random import randint

async def loswy_czas_spania ():
    time_to_sleep = randint(1,10)

    print(f"los: {time_to_sleep}")
    await asyncio.sleep(time_to_sleep)
    return time_to_sleep

async def main ():

    list = [asyncio.create_task (loswy_czas_spania()) for i in range(0,5)]

    a, b = await asyncio.wait(list, return_when=asyncio.FIRST_COMPLETED)


    # print (a)
    # print("______")
    # print (b)

    print (a.pop())

asyncio.run(main())