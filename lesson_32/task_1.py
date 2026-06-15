"""
Kalkulator opóźnień — napisz główną korutynę main, która uruchomi
3 symulowane zadania asyncio.sleep z opóźnieniami:
1 s, 4 s oraz 2 s, używając asyncio.gather().
Program powinien wypisać całkowity czas wykonania (bliski 4 sekund).
"""

import asyncio
import time

async def zadanie(opoznienie):
    await asyncio.sleep(opoznienie)
    return opoznienie

async def main():
    start = time.time()

    wyniki = await asyncio.gather(
        zadanie(1),
        zadanie(4),
        zadanie(2)
    )

    end = time.time()
    print("Zakończone zadania:", wyniki)
    print(f"Czas wykonania: {end - start:.2f} s")

asyncio.run(main())
