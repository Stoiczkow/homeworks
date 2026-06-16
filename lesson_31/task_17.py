import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika):
    print(f"Pobieram ID użytkownika: {nazwa_uzytkownika}")
    await asyncio.sleep(1)

    return 123


async def pobierz_posty(id_uzytkownika):
    print(f"Pobieram posty użytkownika o ID: {id_uzytkownika}")
    await asyncio.sleep(1)

    return [10, 20, 30, 40]


async def pobierz_komentarze(id_postu):
    print(f"Pobieram komentarze dla posta ID: {id_postu}")
    await asyncio.sleep(1)

    return [
        f"Komentarz 1 do posta {id_postu}",
        f"Komentarz 2 do posta {id_postu}",
    ]


async def main():
    start_time = time.time()

    id_uzytkownika = await pobierz_id_uzytkownika("daniel")
    posty = await pobierz_posty(id_uzytkownika)

    zadania_komentarzy = []

    for id_postu in posty:
        task = asyncio.create_task(pobierz_komentarze(id_postu))
        zadania_komentarzy.append(task)

    komentarze = await asyncio.gather(*zadania_komentarzy)

    print("\n--- Wyniki ---")
    print(f"ID użytkownika: {id_uzytkownika}")
    print(f"Posty: {posty}")
    print(f"Komentarze: {komentarze}")

    end_time = time.time()
    print(f"\nCałkowity czas wykonania: {end_time - start_time:.2f}s")


asyncio.run(main())