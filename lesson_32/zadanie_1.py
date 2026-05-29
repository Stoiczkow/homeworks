"""
Zadanie 1 – Kalkulator opóźnień
asyncio.gather uruchamia 3 zadania współbieżnie – całkowity czas ≈ max(1, 4, 2) = 4s.
"""
import asyncio
import time


async def main():
    start = time.perf_counter()

    await asyncio.gather(
        asyncio.sleep(1),
        asyncio.sleep(4),
        asyncio.sleep(2),
    )

    czas = time.perf_counter() - start
    print(f"Całkowity czas wykonania: {czas:.2f}s  (oczekiwany ≈ 4s)")


asyncio.run(main())
