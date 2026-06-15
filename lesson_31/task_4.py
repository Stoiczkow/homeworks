"""
Zmodyfikuj poprzedni kod tak, aby obie korutyny uruchamiały się współbieżnie
za pomocą asyncio.gather(). Zmierz i porównaj czas wykonania.
"""

import asyncio
import time

async def zadanie1():
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone")

async def zadanie2():
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone")

async def main():
    start = time.time()

    # uruchomienie współbieżne
    await asyncio.gather(
        zadanie1(),
        zadanie2()
    )

    end = time.time()
    print(f"Czas wykonania współbieżnego: {end - start:.2f} s")

asyncio.run(main())
