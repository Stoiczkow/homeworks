"""
Zadanie:
Napisz program, który przyjmuje listę adresów URL i współbieżnie sprawdza
status HTTP każdego z nich, używając aiohttp oraz asyncio.gather().
Dla każdego URL wypisz jego status, np.:
"https://google.com - Status: 200"
"""

import asyncio
import aiohttp

async def sprawdz_status(session, url):
    try:
        async with session.get(url) as response:
            return url, response.status
    except Exception as e:
        return url, f"Błąd: {e}"

async def main():
    urls = [
        "https://google.com",
        "https://python.org",
        "https://github.com",
        "https://facebook.com",
        "https://wikipedia.org"
    ]

    async with aiohttp.ClientSession() as session:
        wyniki = await asyncio.gather(
            *(sprawdz_status(session, url) for url in urls)
        )

    for url, status in wyniki:
        print(f"{url} - Status: {status}")

asyncio.run(main())
