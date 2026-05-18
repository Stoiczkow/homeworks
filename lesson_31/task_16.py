# 16. 🧠 Ogranicznik zapytań (Rate Limiter)
# Stwórz klasę RateLimiter z metodą acquire(). Klasa powinna pozwalać na wykonanie
# acquire() tylko n razy na sekundę. Jeśli limit jest przekroczony, acquire() powinno
# asynchronicznie czekać tyle, ile trzeba, by kolejne wywołanie było dozwolone. Przetestuj,
# tworząc 20 zadań, które próbują wywołać acquire() w pętli, z ograniczeniem np. do 5
# zapytań/sekundę.
# (challenge)

import asyncio
import time



class RateLimiter:
    

    async def acquire(self):
        async with self.lock:
            now = time.monotonic()

