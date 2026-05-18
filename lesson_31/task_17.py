# 17. 🧠 Łańcuch zależności
# Stwórz łańcuch zależnych od siebie korutyn:
# 1. pobierz_id_uzytkownika(nazwa_uzytkownika) -> zwraca ID po 1s.
# 2. pobierz_posty(id_uzytkownika) -> zwraca listę ID postów po 1s.
# 3. pobierz_komentarze(id_postu) -> zwraca listę komentarzy po 1s.
# Napisz main, które dla nazwy użytkownika pobierze jego ID, następnie listę jego
# postów, a na końcu pobierze komentarze dla wszystkich jego postów współbieżnie.
# Zmierz czas wykonania.
# (challenge)

import asyncio
import time

async def pobierz_id_uzytkownika(nazwa_uzytkownika):
    await asyncio.sleep(1)
    print(f"Pobrano ID użytkownika: {nazwa_uzytkownika}.")

    return 1

async def pobierz_posty(id_uzytkownika):
    await asyncio.sleep(1)
    print(f"Posty użytkownia {id_uzytkownika}:")

    return ["Post 1", "Post 2", "Post 3"]

async def pobierz_komentarze(id_postu):
    await asyncio.sleep(1)
    
    komentarze = [
        f"Komentarz 1 dla postu {id_postu}",
        f"Komentarz 2 dla postu {id_postu}",
        f"Komentarz 3 dla postu {id_postu}",
    ]

    print(f"Komentarze dla postu {id_postu}")

    return komentarze

async def main():
    start = time.time()

    user_id = await pobierz_id_uzytkownika("Marek")
    posty = await pobierz_posty(user_id)
    tasks = [
        pobierz_komentarze(post)
        for post in posty
    ]

    comments = await asyncio.gather(*tasks)

    end = time.time()

    print("\nKomentarze:")
    print(comments)

    print(f"\nCzas wykonania: {end - start:.2f} s")


asyncio.run(main())

