# Wiele miast
# Używając korutyny z zadania 6, napisz program, który współbieżnie pobierze dane
# pogodowe dla listy miast: ["Warszawa", "Kraków", "Gdańsk"] i wydrukuje wyniki

import asyncio


async def pobierz_pogode(miasto, time_to_sleep):
    await asyncio.sleep(time_to_sleep)
    return {"miasto": miasto, "temperatura": 25, "stan": "słonecznie"}


async def main():
    results = await asyncio.gather(
        pobierz_pogode("Warszawa", 5),
        pobierz_pogode("Kraków", 2),
        pobierz_pogode("Poznań", 1),
    )
    print(results)


asyncio.run(main())