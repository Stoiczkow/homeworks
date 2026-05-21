# Stwórz klasę RateLimiter z metodą acquire(). Klasa powinna pozwalać na wykonanie
# acquire() tylko n razy na sekundę. Jeśli limit jest przekroczony, acquire() powinno
# asynchronicznie czekać tyle, ile trzeba, by kolejne wywołanie było dozwolone. Przetestuj,
# tworząc 20 zadań, które próbują wywołać acquire() w pętli, z ograniczeniem np. do 5
# zapytań/sekundę

import asyncio, time

class RateLimiter:
    def __init__(self, max_calls):
        self.max_calls = max_calls
        self.call_times = []
        self.lock = asyncio.Lock()
        
    async def acquire(self):
        async with self.lock:
            now = time.time()
            
            self.call_times = [time for time in self.call_times if now - time < 1]
                
            if len(self.call_times) >= self.max_calls:
                wait_time = 1 - (now - self.call_times[0])
                await asyncio.sleep(wait_time)
                
                now = time.time()
                self.call_times = [time for time in self.call_times if now - time < 1]

            self.call_times.append(time.time())

async def task(task_id, limiter):
    for i in range(4):
        await limiter.acquire()
        print(f"Task {task_id} wykonał request {i+1}")

async def main():
    rate_limiter = RateLimiter(5)
    
    tasks = [task(i, rate_limiter) for i in range (20)]
    await asyncio.gather(*tasks)

asyncio.run(main())