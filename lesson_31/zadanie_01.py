import asyncio


async def przywitanie() -> None:
    print("Gotowy do nauki asyncio!")


if __name__ == "__main__":
    asyncio.run(przywitanie())
