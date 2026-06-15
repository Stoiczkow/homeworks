"""
Stwórz dwie korutyny: zadanie1 śpi 2 sekundy i drukuje "Zadanie 1 zakończone",
a zadanie2 śpi 1 sekundę i drukuje "Zadanie 2 zakończone".
W korutynie main uruchom je SEKWENCYJNIE (await jedno po drugim)
i zmierz czas wykonania.
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

    await zadanie1()   
    await zadanie2()  

    end = time.time()
    print(f"Czas wykonania sekwencyjnego: {end - start:.2f} s")

asyncio.run(main())
