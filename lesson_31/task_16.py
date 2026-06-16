import asyncio
import time
from collections import deque


class RateLimiter:
    def __init__(self, limit_per_second):
        self.limit_per_second = limit_per_second
        self.calls = deque()
        self.lock = asyncio.Lock()

    async def acquire(self):
        async with self.lock:
            now = time.monotonic()

            while self.calls and now - self.calls[0] >= 1:
                self.calls.popleft()

            if len(self.calls) >= self.limit_per_second:
                wait_time = 1 - (now - self.calls[0])
                await asyncio.sleep(wait_time)

                now = time.monotonic()

                while self.calls and now - self.calls[0] >= 1:
                    self.calls.popleft()

            self.calls.append(time.monotonic())


async def worker(number, limiter, start_time):
    await limiter.acquire()

    current_time = time.monotonic() - start_time
    print(f"Zadanie {number} wykonało zapytanie po {current_time:.2f}s")


async def main():
    limiter = RateLimiter(limit_per_second=5)
    start_time = time.monotonic()

    tasks = []

    for i in range(1, 21):
        task = asyncio.create_task(worker(i, limiter, start_time))
        tasks.append(task)

    await asyncio.gather(*tasks)


asyncio.run(main())