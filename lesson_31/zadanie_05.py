import asyncio


async def oblicz_potege(liczba: int, potega: int) -> int:
    await asyncio.sleep(2)
    return liczba ** potega


async def main() -> None:
    wynik = await oblicz_potege(2, 10)
    print(f"Wynik: {wynik}")


if __name__ == "__main__":
    asyncio.run(main())
