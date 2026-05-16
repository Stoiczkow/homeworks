# Pobieranie statusów HTTP

# Napisz program, który przyjmuje listę adresów URL i współbieżnie sprawdza status HTTP każdego z nich. Użyj biblioteki aiohttp. Wskazówka: musisz ją zainstalować (pip install aiohttp) i użyć aiohttp.ClientSession. Dla każdego URL wypisz jego status (np. "https://google.com - Status: 200")

import asyncio

import aiohttp


async def check_status(host):
    client = aiohttp.ClientSession()
    result = await client.get(host)
    await client.close()
    return f"Strona {host} odpowiada statusem {result.status}"


async def main():
    tasks = asyncio.gather(
        check_status("http://wp.pl"),
        check_status("http://onet.pl"),
        check_status("http://gazeta.pl"),
        check_status("http://republika.pl"),
        check_status("http://tvp.pl"),
        check_status("http://tvp.pl/asdadadasdasd"),
    )

    results = await tasks

    for result in results:
        print(result)


asyncio.run(main())