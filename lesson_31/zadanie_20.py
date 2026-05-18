import asyncio
import random


async def dlugie_zadanie() -> str:
    czas = random.uniform(1, 5)
    print(f"Zadanie zaplanowane na {czas:.2f}s")
    await asyncio.sleep(czas)
    return f"Zakończono po {czas:.2f}s"


async def main() -> None:
    try:
        wynik = await asyncio.wait_for(dlugie_zadanie(), timeout=3.0)
        print(f"Wynik: {wynik}")
    except asyncio.TimeoutError:
        print("Przekroczono limit czasu 3s - zadanie anulowane.")


if __name__ == "__main__":
    asyncio.run(main())
