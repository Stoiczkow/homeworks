import asyncio
import random


async def ping(host: str) -> str:
    await asyncio.sleep(random.uniform(0.1, 1.0))
    return f"Host {host} odpowiada"


async def main() -> None:
    hosty = ["google.com", "github.com", "wp.pl", "onet.pl", "python.org"]
    wyniki = await asyncio.gather(*(ping(h) for h in hosty))
    for wynik in wyniki:
        print(wynik)


if __name__ == "__main__":
    asyncio.run(main())
