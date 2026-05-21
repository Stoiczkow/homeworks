import asyncio
from random import uniform


async def ping(host):
    ping_time = uniform(0.1, 1.0)
    await asyncio.sleep(ping_time)
    return f"Host {host} odpowiada w czasie {ping_time}"


async def main():
    tasks = asyncio.gather(
        ping("wp.pl"),
        ping("onet.pl"),
        ping("gazeta.pl"),
        ping("republika.pl"),
        ping("tvp.pl"),
    )

    results = await tasks

    for result in results:
        print(result)


asyncio.run(main())