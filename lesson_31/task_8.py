"""
Napisz korutynę ping(host), która symuluje pingowanie serwera przez
asyncio.sleep(random.uniform(0.1, 1.0)) i zwraca napis "Host {host} odpowiada".
Uruchom ją współbieżnie dla 5 różnych hostów.
"""

import asyncio
import random

async def ping(host):
    await asyncio.sleep(random.uniform(0.1, 1.0))
    return f"Host {host} odpowiada"

async def main():
    hosts = ["A", "B", "C", "D", "E"]

    wyniki = await asyncio.gather(
        *(ping(h) for h in hosts)
    )

    for wynik in wyniki:
        print(wynik)

asyncio.run(main())
