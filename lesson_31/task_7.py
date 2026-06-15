"""
Używając korutyny pobierz_pogode(miasto) z poprzedniego zadania,
napisz program, który współbieżnie pobierze dane pogodowe dla listy:
["Warszawa", "Kraków", "Gdańsk"] i wydrukuje wyniki.
"""

import asyncio

async def pobierz_pogode(miasto):
    await asyncio.sleep(1.5)
    return {
        "miasto": miasto,
        "temperatura": 25,
        "stan": "słonecznie"
    }

async def main():
    miasta = ["Warszawa", "Kraków", "Gdańsk"]

    wyniki = await asyncio.gather(
        *(pobierz_pogode(m) for m in miasta)
    )

    for wynik in wyniki:
        print(wynik)

asyncio.run(main())
