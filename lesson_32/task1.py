# (Proste) Kalkulator opóźnień: Napisz główną korutynę main , która uruchomi 3
# symulowane zadania asyncio.sleep (z opóźnieniami 1, 4, 2 sekundy) używając
# asyncio.gather . Program powinien wypisać całkowity czas wykonania (powinien być
# bliski 4 sekund)

import asyncio
import time

tasks = [
    asyncio.sleep(1),
    asyncio.sleep(4),
    asyncio.sleep(2)
    
]
async def main():
    print("start")
    start_time = time.time()
    await asyncio.gather(*tasks)
    end_time = time.time()
    print("stop")
    print(f"Całkowity czas wykonania to: {end_time - start_time} s")
    
asyncio.run(main())