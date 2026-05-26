# Generator liczb pierwszych
# Napisz asynchroniczny generator, który co pewien czas (np. 0.1s) "produkuje" kolejną
# liczbę pierwszą. W głównej pętli iteruj po tym generatorze za pomocą async for i wypisuj
# liczby, aż dojdziesz do 100.

import asyncio

from sympy import nextprime

async def generator(n):
    iterations = n
    value = nextprime(0)
    
    for _ in range(iterations):
        await asyncio.sleep(0.1)
        value = nextprime(value)
        yield value

async def main():
    async for value in generator(100):
        print(value)

asyncio.run(main())