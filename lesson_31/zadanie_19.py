import asyncio
from typing import AsyncIterator


def czy_pierwsza(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    dzielnik = 3
    while dzielnik * dzielnik <= n:
        if n % dzielnik == 0:
            return False
        dzielnik += 2
    return True


async def generator_liczb_pierwszych(limit: int) -> AsyncIterator[int]:
    liczba = 2
    while liczba <= limit:
        if czy_pierwsza(liczba):
            await asyncio.sleep(0.1)
            yield liczba
        liczba += 1


async def main() -> None:
    async for p in generator_liczb_pierwszych(100):
        print(p)


if __name__ == "__main__":
    asyncio.run(main())
