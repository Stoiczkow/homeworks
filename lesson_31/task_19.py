# 19. 🧠 Generator liczb pierwszych
# Napisz asynchroniczny generator, który co pewien czas (np. 0.1s) "produkuje" kolejną
# liczbę pierwszą. W głównej pętli iteruj po tym generatorze za pomocą async for i wypisuj
# liczby, aż dojdziesz do 100.
# (challenge)

import asyncio

def liczby_pierwsze(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

async def generuj_liczby_pierwsze(max):
    liczba = 2

    while liczba <= max:
        if liczby_pierwsze(liczba):
            await asyncio.sleep(0.1)
            yield liczba

        liczba += 1

async def main():
    async for p in generuj_liczby_pierwsze(100):
        print(p)

asyncio.run(main())