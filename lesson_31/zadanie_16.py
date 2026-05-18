import asyncio
import time
from collections import deque


class RateLimiter:
    def __init__(self, limit: int, okno: float = 1.0) -> None:
        self.limit = limit
        self.okno = okno
        self._znaczniki: deque[float] = deque()
        self._lock = asyncio.Lock()

    async def acquire(self) -> None:
        async with self._lock:
            teraz = time.monotonic()
            while self._znaczniki and teraz - self._znaczniki[0] >= self.okno:
                self._znaczniki.popleft()

            if len(self._znaczniki) >= self.limit:
                czas_oczekiwania = self.okno - (teraz - self._znaczniki[0])
                await asyncio.sleep(czas_oczekiwania)
                teraz = time.monotonic()
                while self._znaczniki and teraz - self._znaczniki[0] >= self.okno:
                    self._znaczniki.popleft()

            self._znaczniki.append(teraz)


async def zadanie(numer: int, limiter: RateLimiter, start: float) -> None:
    await limiter.acquire()
    print(f"Zadanie {numer} wykonane o czasie {time.monotonic() - start:.2f}s")


async def main() -> None:
    limiter = RateLimiter(limit=5, okno=1.0)
    start = time.monotonic()
    await asyncio.gather(*(zadanie(i, limiter, start) for i in range(1, 21)))
    print(f"\nŁączny czas: {time.monotonic() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
