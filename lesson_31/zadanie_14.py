import asyncio


async def producent(kolejka: asyncio.Queue[int]) -> None:
    for liczba in range(1, 21):
        await asyncio.sleep(0.5)
        await kolejka.put(liczba)
        print(f"Producent dodał: {liczba}")
    await kolejka.put(None)
    await kolejka.put(None)


async def konsument(numer: int, kolejka: asyncio.Queue[int]) -> None:
    while True:
        liczba = await kolejka.get()
        if liczba is None:
            kolejka.task_done()
            break
        print(f"Konsument {numer} przetworzył liczbę: {liczba}")
        kolejka.task_done()


async def main() -> None:
    kolejka: asyncio.Queue[int] = asyncio.Queue()
    await asyncio.gather(
        producent(kolejka),
        konsument(1, kolejka),
        konsument(2, kolejka),
    )


if __name__ == "__main__":
    asyncio.run(main())
