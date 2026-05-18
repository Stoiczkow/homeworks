# 11. 🧠 Sumowanie wyników zadań
# Napisz korutynę dlugie_obliczenia(), która po losowym czasie (od 2 do 5 sekund) zwraca
# losową liczbę całkowitą (od 1 do 100). Uruchom 10 takich zadań współbieżnie i po
# zakończeniu wszystkich oblicz i wypisz sumę ich wyników.
# (challenge)


import asyncio
from random import randint


async def dlugie_obliczenia():
    await asyncio.sleep(randint(2, 5))
    return randint(1, 100)


async def main():
    tasks_to_run = [dlugie_obliczenia() for x in range(0, 10)]
    tasks = asyncio.gather(*tasks_to_run)

    results = await tasks
    print(results)

    print(f"Suma {sum(results)}")


asyncio.run(main())