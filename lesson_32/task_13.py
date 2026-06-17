import asyncio
import aiohttp


async def fetch(session, url):
    print(f"Pobieram: {url}")

    async with session.get(url) as response:
        if response.status != 200:
            text = await response.text()
            return {
                "url": url,
                "status": response.status,
                "error": text[:200],
            }

        data = await response.json()

        return {
            "url": url,
            "status": response.status,
            "data": data,
        }


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ]

    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            fetch(session, urls[0]),
            fetch(session, urls[1]),
            fetch(session, urls[2]),
        )

    print("\nWyniki:")

    for result in results:
        print("-" * 40)
        print("URL:", result["url"])
        print("Status:", result["status"])
        print("Dane:", result["data"])


if __name__ == "__main__":
    asyncio.run(main())
    