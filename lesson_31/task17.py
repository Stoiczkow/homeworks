# 17 Łańcuch zależności

# Stwórz łańcuch zależnych od siebie korutyn:
# 1. pobierz_id_uzytkownika(nazwa_uzytkownika) -> zwraca ID po 1s.
# 2. pobierz_posty(id_uzytkownika) -> zwraca listę ID postów po 1s.
# 3. pobierz_komentarze(id_postu) -> zwraca listę komentarzy po 1s.
# Napisz main, które dla nazwy użytkownika pobierze jego ID, następnie listę jego
# postów, a na końcu pobierze komentarze dla wszystkich jego postów współbieżnie.
# Zmierz czas wykonania

import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika: str) -> int:
    await asyncio.sleep(1)
    return hash(nazwa_uzytkownika) % 1000


async def pobierz_posty(id_uzytkownika: int) -> list[int]:
    await asyncio.sleep(1)
    return [id_uzytkownika * 10 + i for i in range(5)]


async def pobierz_komentarze(id_postu: int) -> list[str]:
    await asyncio.sleep(1)
    return [f"Komentarz {i} do posta {id_postu}" for i in range(3)]


async def main():
    start = time.perf_counter()

    user_id = await pobierz_id_uzytkownika("Janusz_Janusz")
    print(f"User ID: {user_id}")

    posty = await pobierz_posty(user_id)
    print(f"Posty: {posty}")

    # równoległe pobieranie komentarzy dla wszystkich postów
    tasks = [pobierz_komentarze(post_id) for post_id in posty]
    komentarze = await asyncio.gather(*tasks)


    wszystkie_komentarze = [k for sublist in komentarze for k in sublist]

    print("\nKomentarze:")
    for k in wszystkie_komentarze:
        print(k)

    end = time.perf_counter()

    print(f"\nCzas wykonania: {end - start:.2f} s")


if __name__ == "__main__":
    asyncio.run(main())