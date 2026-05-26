# Ogranicznik zapytań (Rate Limiter)
# Stwórz klasę RateLimiter z metodą acquire(). Klasa powinna pozwalać na wykonanie
# acquire() tylko n razy na sekundę. Jeśli limit jest przekroczony, acquire() powinno
# asynchronicznie czekać tyle, ile trzeba, by kolejne wywołanie było dozwolone. Przetestuj,
# tworząc 20 zadań, które próbują wywołać acquire() w pętli, z ograniczeniem np. do 5
# zapytań/sekundę.

import asyncio
import time

class RateLimiter:
    def __init__(self, n: int):
        self.limit = n
        self.used_limit = 0
        self.time_window = None

    async def acquire(self):
        while True:
            current_time = time.time()

            if not self.time_window or current_time > self.time_window:
                self.time_window = current_time + 1
                self.used_limit = 0

            if self.used_limit < self.limit:
                self.used_limit += 1
                print(f"Zadanie wykonane. Obecny stan limitu: {self.used_limit}")
                break
            else:
                time_to_wait = self.time_window - time.time()
                await asyncio.sleep(time_to_wait)


r1 = RateLimiter(3)

tasks_list = [r1.acquire() for x in range(1,21)]

async def main():

    tasks = asyncio.gather(*tasks_list)

    await tasks

asyncio.run(main())

