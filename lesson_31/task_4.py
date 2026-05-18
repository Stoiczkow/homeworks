# 4. ✏ Dwa zadania współbieżnie
# Zmodyfikuj kod z poprzedniego zadania. Uruchom obie korutyny współbieżnie, używając
# asyncio.gather(). Zmierz i porównaj czas wykonania.

import asyncio
import time


async def zadanie1():
    await asyncio.sleep(2)
    print("Zadanie 1 zakończone.")

async def zadanie2():
    await asyncio.sleep(1)
    print("Zadanie 2 zakończone.")

async def main():
    start = time.time()

    # await zadanie1()
    # await zadanie2()
    
    await asyncio.gather(
        zadanie1(),
        zadanie2()
    )

    end = time.time()

    print(f"Czas wykonania: ({end - start:.2f})")

asyncio.run(main())