import asyncio


async def oblicz_potege(liczba, potega):
    await asyncio.sleep(2)
    return liczba**potega


async def main():
    result = await oblicz_potege(2, 3)
    print(result)


asyncio.run(main())