import asyncio


async def licznik(n: int) -> None:
    for i in range(1, n + 1):
        await asyncio.sleep(1)
        print(i)


if __name__ == "__main__":
    asyncio.run(licznik(5))
