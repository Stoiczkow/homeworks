# Współbieżne odliczanie

# Napisz korutynę odliczanie(nazwa, start), która co sekundę drukuje komunikat "{nazwa}: zostało {pozostało} sekund". Uruchom trzy takie odliczania współbieżnie, każde z inną nazwą i innym czasem początkowym (np. 5s, 3s, 7s)


import asyncio


async def odliczanie(nazwa, start):
    for i in list(range(0, start))[::-1]:
        print(f"{nazwa} zostało {i} sekund")
        await asyncio.sleep(1)


async def main():
    tasks = asyncio.gather(
        odliczanie("Zadanie 1", 5),
        odliczanie("Zadanie 2", 3),
        odliczanie("Zadanie 3", 7),
    )

    await tasks


asyncio.run(main())