# 12. 🧠 Kto pierwszy, ten lepszy
# Uruchom 5 zadań, z których każde śpi przez losowy czas (od 1 do 10 sekund), a następnie
# zwraca swój czas uśpienia. Napisz program, który zakończy działanie i wypisze wynik
# pierwszego zakończonego zadania, nie czekając na pozostałe. Wskazówka: użyj
# asyncio.wait() z argumentem return_when=asyncio.FIRST_COMPLETED.
# (challenge)

import asyncio
from random import randint


async def losowy_czas_spania ():
    time_to_sleep = randint(1,10)

    print(f"los: {time_to_sleep}")
    await asyncio.sleep(time_to_sleep)
    return time_to_sleep

async def main ():

    list = [asyncio.create_task (losowy_czas_spania()) for i in range(0,5)]

    a, b = await asyncio.wait(list, return_when=asyncio.FIRST_COMPLETED)



    print (a.pop())

asyncio.run(main())

