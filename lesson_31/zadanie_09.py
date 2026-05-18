import asyncio

import aiohttp


async def sprawdz_status(session: aiohttp.ClientSession, url: str) -> None:
    try:
        async with session.get(url) as response:
            print(f"{url} - Status: {response.status}")
    except aiohttp.ClientError as exc:
        print(f"{url} - Błąd: {exc}")


async def main() -> None:
    urls = [
        "https://google.com",
        "https://github.com",
        "https://python.org",
        "https://httpbin.org/status/404",
        "https://httpbin.org/status/500",
    ]
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*(sprawdz_status(session, url) for url in urls))


if __name__ == "__main__":
    asyncio.run(main())
