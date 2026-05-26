# Stwórz łańcuch zależnych od siebie korutyn:
# 1. pobierz_id_uzytkownika(nazwa_uzytkownika) -> zwraca ID po 1s.
# 2. pobierz_posty(id_uzytkownika) -> zwraca listę ID postów po 1s.
# 3. pobierz_komentarze(id_postu) -> zwraca listę komentarzy po 1s.
# Napisz main, które dla nazwy użytkownika pobierze jego ID, następnie listę jego
# postów, a na końcu pobierze komentarze dla wszystkich jego postów współbieżnie.
# Zmierz czas wykonania.

import asyncio
import time

async def pobierz_id_uzytkownika(nazwa_uzytkownika):
    await asyncio.sleep(1)
    return 10

async def pobierz_posty(id_uzytkownika):
    await asyncio.sleep(1)
    return ["Post1", "Post2", "Post3"]

async def pobierz_komentarze(id_postu):
    await asyncio.sleep(1)
    match id_postu:
        case "Post1":
            return ["p_1Comment1", "p_1Comment2", "p_1Comment3"]
        case "Post2":
            return ["p_2Comment1", "p_2Comment2", "p_2Comment3"]
        case "Post3":
            return ["p_3Comment1", "p_3Comment2", "p_3Comment3"]

async def main(nazwa_uzytkownika):
    start_time = time.time()
    id_uzytkownika = await pobierz_id_uzytkownika(nazwa_uzytkownika)

    posty = await pobierz_posty(id_uzytkownika)

    tasks = [pobierz_komentarze(post) for post in posty]
    comments = await asyncio.gather(*tasks)

    print(comments)
    task_time = time.time() - start_time
    print(f"Wykonanie zadań zajęło {task_time}")


asyncio.run(main("Test"))