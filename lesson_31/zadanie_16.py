"""
Zadanie 16 – Ogranicznik zapytań (Rate Limiter)
RateLimiter.acquire() pozwala na co najwyżej n wywołań na sekundę.
Jeśli limit jest przekroczony, acquire() asynchronicznie czeka.
"""
import asyncio
import time


class RateLimiter:
    def __init__(self, max_per_second: int):
        self.max_per_second = max_per_second
        self._interwał = 1.0 / max_per_second
        self._ostatnie_wywolanie = 0.0
        self._lock = asyncio.Lock()

    async def acquire(self):
        async with self._lock:
            teraz = time.monotonic()
            czas_od_ostatniego = teraz - self._ostatnie_wywolanie
            if czas_od_ostatniego < self._interwał:
                await asyncio.sleep(self._interwał - czas_od_ostatniego)
            self._ostatnie_wywolanie = time.monotonic()


async def zadanie(numer, limiter):
    await limiter.acquire()
    print(f"[{time.monotonic():.3f}] Zadanie {numer:02d} wykonane")


async def main():
    LIMIT = 5  # 5 zapytań/sekundę
    limiter = RateLimiter(max_per_second=LIMIT)

    start = time.monotonic()
    await asyncio.gather(*[zadanie(i, limiter) for i in range(1, 21)])
    czas = time.monotonic() - start

    print(f"\n20 zadań przy limicie {LIMIT}/s ukończono w {czas:.2f}s")
    print(f"(oczekiwany czas ≈ {20 / LIMIT:.1f}s)")


asyncio.run(main())
