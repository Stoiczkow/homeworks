import asyncio
import time
import random
import aiohttp
from random import randint
#task1
# async def hello():
#     print("Gotowy do nauki asyncio")

# asyncio.run(hello())

#task2


# async def licznik(n):

#     for i in range(n):
#         print(f"{i}")
#         await asyncio.sleep(1)

# asyncio.run(licznik(7))

#task3

# twórz dwie korutyny: zadanie1 śpi przez 2 sekundy i drukuje "Zadanie 1 zakończone", a
# zadanie2 śpi przez 1 sekundę i drukuje "Zadanie 2 zakończone". W głównej korutynie main
# uruchom je sekwencyjnie (używając await na każdej z nich po kolei) i zmierz czas
# wykonania.


# import asyncio
# import time

# async def zadanie1():
#     await asyncio.sleep(2)
#     print("Zadanie 1 zakończone")

# async def zadanie2():
#     await asyncio.sleep(1)
#     print("Zadanie 2 zakończone")

# async def main():
#     start = time.time()

#     await zadanie1()
#     await zadanie2()

#     stop = time.time()

#     print(f"Czas wykonania: {stop - start}")

# asyncio.run(main())

#task 4


#  Zmodyfikuj kod z poprzedniego zadania. Uruchom obie korutyny współbieżnie, używając
# asyncio.gather(). Zmierz i porównaj czas wykonania

# import asyncio
# import time

# async def zadanie1():
#     await asyncio.sleep(2)
#     print("Zadanie 1 zakończone")

# async def zadanie2():
#     await asyncio.sleep(1)
#     print("Zadanie 2 zakończone")

# async def main():
#     start = time.time()

#     # await zadanie1()
#     # await zadanie2()

#     await asyncio.gather(
#         zadanie1(),
#         zadanie2()
#     )

#     stop = time.time()

#     print(f"Czas wykonania: {stop - start}")

# asyncio.run(main())

#task5

# async def oblicz_potege(liczba, potega):
#     await asyncio.sleep(2)
#     return liczba ** potega

# async def main():
#     result = await oblicz_potege(2,3)
#     print(result)

# asyncio.run(main())

#task6


# async def pobierz_pogode(miasto):
#     await asyncio.sleep(1.5)
#     return {"miasto": miasto, "temperatura": 25, "stan": "słonecznie"}


# async def main():
#     result = await pobierz_pogode("Warszawa")
#     print(result)


# asyncio.run(main())

#7


# async def pobierz_pogode(miasto: str):
#     await asyncio.sleep(1.5)
#     stany = ["slonecznie", "pochmurno", "deszczowo", "wiatr"]

#     result = {"miasto" : miasto,
#                 "temperatura" : random.randrange(14, 30),
#                 "stan" : random.choice(stany)
#                 }

#     return result

# async def main():
    
#     miasta = ["Warszawa", "Kraków", "Gdańsk"]

#     task = [pobierz_pogode(miasto) for miasto in miasta]

#     result = await asyncio.gather(*task) 
#     print(result)   

# if __name__ == "__main__":
#     asyncio.run(main())

#8
# import asyncio
# from random import uniform


# async def ping(host):
#     ping_time = uniform(0.1, 1.0)
#     await asyncio.sleep(ping_time)
#     return f"Host {host} odpowiada w czasie {ping_time}"


# async def main():
#     tasks = asyncio.gather(
#         ping("wp.pl"),
#         ping("onet.pl"),
#         ping("gazeta.pl"),
#         ping("republika.pl"),
#         ping("tvp.pl"),
#     )

#     results = await tasks

#     for result in results:
#         print(result)


# asyncio.run(main())

#9

# async def check_status(host):
#     client = aiohttp.ClientSession()
#     result = await client.get(host)
#     await client.close()
#     return f"Strona {host} odpowiada statusem {result.status}"


# async def main():
#     tasks = asyncio.gather(
#         check_status("http://wp.pl"),
#         check_status("http://onet.pl"),
#         check_status("http://gazeta.pl"),
#         check_status("http://republika.pl"),
#         check_status("http://tvp.pl"),
#         check_status("http://tvp.pl/asdadadasdasd"),
#     )

#     results = await tasks

#     for result in results:
#         print(result)


# asyncio.run(main())

#10
# import asyncio


# async def odliczanie(nazwa, start):
#     for i in list(range(0, start))[::-1]:
#         print(f"{nazwa} zostało {i} sekund")
#         await asyncio.sleep(1)


# async def main():
#     tasks = asyncio.gather(
#         odliczanie("Zadanie 1", 5),
#         odliczanie("Zadanie 2", 3),
#         odliczanie("Zadanie 3", 7),
#     )

#     await tasks


# asyncio.run(main())

#11
# import asyncio
# from random import randint


# async def dlugie_obliczenia():
#     await asyncio.sleep(randint(2, 5))
#     return randint(1, 100)


# async def main():
#     tasks_to_run = [dlugie_obliczenia() for x in range(0, 10)]
#     tasks = asyncio.gather(*tasks_to_run)

#     results = await tasks
#     print(results)

#     print(f"Suma {sum(results)}")


# asyncio.run(main())

#12



# async def loswy_czas_spania ():
#     time_to_sleep = randint(1,10)

#     print(f"los: {time_to_sleep}")
#     await asyncio.sleep(time_to_sleep)
#     return time_to_sleep

# async def main ():

#     list = [asyncio.create_task (loswy_czas_spania()) for i in range(0,5)]

#     a, b = await asyncio.wait(list, return_when=asyncio.FIRST_COMPLETED)


#     # print (a)
#     # print("______")
#     # print (b)

#     print (a.pop())

# asyncio.run(main())

#14

# async def producer(queue):
#     for i in range(1, 21):
#         await asyncio.sleep(0.5)
#         await queue.put(i)


# async def consumer(name, queue):
#     while True:
#         get_from_q = queue.get()

#         try:
#             element = await asyncio.wait_for(get_from_q, timeout=2)
#         except TimeoutError:
#             break

#         print(f"{name} przetworzył liczbę: {element}")


# async def main():
#     queue = asyncio.Queue()
#     await asyncio.gather(
#         producer(queue), consumer("Konsument 1", queue), consumer("Konsument 2", queue)
#     )


# asyncio.run(main())


#15

# import asyncio
# import random
# import aiofiles

# # Nazwa pliku, do którego będą zapisywane logi
# LOG_FILE = "korutyna.txt"

# async def worker(korutyna_id: int, lock: asyncio.Lock, repetitions: int = 5):
#     for i in range(repetitions):
#         await asyncio.sleep(random.uniform(0.1, 0.5))
        
#         log_message = f"Log z korutyny {korutyna_id} - wpis nr {i + 1}\n"
        
#         async with lock:
#             print(f"[Korutyna {korutyna_id}] Uzyskano blokadę. Zapisuję...")
#             async with aiofiles.open(LOG_FILE, mode='a', encoding='utf-8') as f:
#                 await f.write(log_message)
#                 await f.flush() 
        

# async def main():
#     lock = asyncio.Lock()
    
#     async with aiofiles.open(LOG_FILE, mode='w', encoding='utf-8') as f:
#         await f.write("Logowanie")

#     print("Start korutyny")
    
#     tasks = [worker(korutyna_id=i, lock=lock) for i in range(1, 6)]
    
#     await asyncio.gather(*tasks)
    
#     print(f"Koniec - plik zapisany w {LOG_FILE}")

# if __name__ == "__main__":
#     asyncio.run(main())

#18

import asyncio


async def pracuj():
    try:
        while True:
            print("Pracuję...")
            await asyncio.sleep(1)
    except asyncio.CancelledError:
        print("Anulowano, sprzątam...")
        raise   


async def main():
    task = asyncio.create_task(pracuj())


    await asyncio.sleep(5)

    task.cancel()

    try:
        await task
    except asyncio.CancelledError:
        print("Zadanie zostało anulowane.")


asyncio.run(main())



#task19

# import asyncio

# def is_prime(n: int):
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True


# async def generator(delay: float = 0.1):
#     number = 2
#     while True:
#         if is_prime(number):
#             yield number
#             await asyncio.sleep(delay)
#         number += 1


# async def main():
#     print("Generowanie kolejnych liczb pierwszych")

#     async for i in generator(delay=0.1):
#         print(f"Otrzymano: {i}")

#         if i > 100:
#             print("Koniec programu")
#             break


# if __name__ == "__main__":
#     asyncio.run(main())

#20

# import asyncio
# import random


# async def losowy_sen():
#     czas = random.randrange(1, 5)
#     print(f"Korutyna wstzrymana na {czas} sekundy")
#     await asyncio.sleep(czas)
#     print("Korutyna zakończyła działanie")


# async def main():
#     try:
#         await asyncio.wait_for(losowy_sen(), timeout=3)
#     except asyncio.TimeoutError:
#         print("Error: przekroczono czas dzialania programu!!!")


# asyncio.run(main())