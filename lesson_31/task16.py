#Ogranicznik zapytań (Rate Limiter)

# Stwórz klasę RateLimiter z metodą acquire(). Klasa powinna pozwalać na wykonanie
# acquire() tylko n razy na sekundę. Jeśli limit jest przekroczony, acquire() powinno
# asynchronicznie czekać tyle, ile trzeba, by kolejne wywołanie było dozwolone. Przetestuj, tworząc 20 zadań, które próbują wywołać acquire() w pętli, z ograniczeniem np. do 5 zapytań/sekundę

import asyncio
import time
from collections import deque


class RateLimiter:
    def __init__(self, max_calls: int, period: float):
        self.max_calls = max_calls
        self.period = period
        self.calls = deque()
        self.lock = asyncio.Lock()

    async def acquire(self):
        while True:
            async with self.lock:
                now = time.monotonic()

                # usuń stare wywołania
                while self.calls and self.calls[0] <= now - self.period:
                    self.calls.popleft()

              
                if len(self.calls) < self.max_calls:
                    self.calls.append(now)
                    return

                # ile trzeba czekać
                wait_time = self.period - (now - self.calls[0])

            # sleep poza lockiem
            if wait_time > 0:
                await asyncio.sleep(wait_time)


async def worker(name: int, limiter: RateLimiter):
    for i in range(3):
        await limiter.acquire()
        print(f"{time.strftime('%X')} - Task {name} step {i}")


async def main():
    limiter = RateLimiter(max_calls=5, period=1.0)

    tasks = [asyncio.create_task(worker(i, limiter)) for i in range(20)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())