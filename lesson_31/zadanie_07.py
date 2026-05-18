import asyncio


async def pobierz_pogode(miasto: str) -> dict[str, str | int]:
    await asyncio.sleep(1.5)
    return {"miasto": miasto, "temperatura": 25, "stan": "słonecznie"}


async def main() -> None:
    miasta = ["Warszawa", "Kraków", "Gdańsk"]
    wyniki = await asyncio.gather(*(pobierz_pogode(m) for m in miasta))
    for wynik in wyniki:
        print(wynik)


if __name__ == "__main__":
    asyncio.run(main())
