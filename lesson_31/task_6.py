import asyncio


async def pobierz_pogode(miasto):
    await asyncio.sleep(1.5)
    return {"miasto": miasto, "temperatura": 25, "stan": "słonecznie"}


async def main():
    result = await pobierz_pogode("Warszawa")
    print(result)


asyncio.run(main())