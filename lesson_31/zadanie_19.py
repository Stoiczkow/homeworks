"""
Zadanie 19 – Asynchroniczny generator liczb pierwszych
Generator co 0.1s produkuje kolejną liczbę pierwszą.
Pętla async for przerywa, gdy liczba przekroczy 100.
"""
import asyncio


def czy_pierwsza(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


async def generator_pierwszych():
    kandydat = 2
    while True:
        if czy_pierwsza(kandydat):
            await asyncio.sleep(0.1)
            yield kandydat
        kandydat += 1


async def main():
    pierwsze = []
    async for liczba in generator_pierwszych():
        if liczba > 100:
            break
        pierwsze.append(liczba)
        print(liczba, end=' ', flush=True)
    print(f"\n\nLiczby pierwsze do 100 ({len(pierwsze)} szt.): {pierwsze}")


asyncio.run(main())
