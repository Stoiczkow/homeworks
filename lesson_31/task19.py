# Generator liczb pierwszych

# Napisz asynchroniczny generator, który co pewien czas (np. 0.1s) "produkuje" kolejną liczbę pierwszą. W głównej pętli iteruj po tym generatorze za pomocą async for i wypisuj liczby, aż dojdziesz do 100.

import asyncio
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(math.sqrt(n)) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True


class AsyncPrimeGenerator:
    def __init__(self, delay: float = 0.1):
        self.delay = delay
        self.current = 1

    def __aiter__(self):
        return self

    async def __anext__(self):
        while True:
            self.current += 1

            if is_prime(self.current):
                await asyncio.sleep(self.delay)
                return self.current


async def main():
    primes = AsyncPrimeGenerator(delay=0.1)

    async for p in primes:
        print(p)
        if p >= 100:
            break


if __name__ == "__main__":
    asyncio.run(main())