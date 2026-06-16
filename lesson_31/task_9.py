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