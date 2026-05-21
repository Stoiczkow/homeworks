# Generator liczb pierwszych
# Napisz asynchroniczny generator, który co pewien czas (np. 0.1s) "produkuje" kolejną
# liczbę pierwszą. W głównej pętli iteruj po tym generatorze za pomocą async for i wypisuj
# liczby, aż dojdziesz do 100.

import asyncio
import math

def is_prime(number: int):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True
    
async def generator(limit=200):
    n = 1
    
    while n <= limit:
        if is_prime(n):
            yield n
            await asyncio.sleep(0.1)
            
        n += 2       
        
async def main():
    async for i in generator():
            print(i)
            
asyncio.run(main())