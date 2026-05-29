"""
Zadanie 17 – Łańcuch zależności
1. pobierz_id_uzytkownika(nazwa) → ID po 1s
2. pobierz_posty(user_id)        → lista ID postów po 1s
3. pobierz_komentarze(post_id)   → lista komentarzy po 1s
Komentarze dla wszystkich postów pobierane współbieżnie (asyncio.gather).
"""
import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika: str) -> int:
    await asyncio.sleep(1)
    user_id = abs(hash(nazwa_uzytkownika)) % 1000
    print(f"ID użytkownika '{nazwa_uzytkownika}': {user_id}")
    return user_id


async def pobierz_posty(id_uzytkownika: int) -> list[int]:
    await asyncio.sleep(1)
    posty = [id_uzytkownika * 10 + i for i in range(1, 4)]
    print(f"Posty użytkownika {id_uzytkownika}: {posty}")
    return posty


async def pobierz_komentarze(id_postu: int) -> list[str]:
    await asyncio.sleep(1)
    komentarze = [f"Komentarz {i} do postu {id_postu}" for i in range(1, 3)]
    return komentarze


async def main():
    nazwa = "jan_kowalski"
    start = time.perf_counter()

    # Krok 1 i 2 muszą być sekwencyjne (zależność)
    user_id = await pobierz_id_uzytkownika(nazwa)
    posty = await pobierz_posty(user_id)

    # Krok 3 – komentarze dla wszystkich postów współbieżnie
    wszystkie_komentarze = await asyncio.gather(
        *[pobierz_komentarze(post_id) for post_id in posty]
    )

    for post_id, komentarze in zip(posty, wszystkie_komentarze):
        print(f"Post {post_id}: {komentarze}")

    czas = time.perf_counter() - start
    print(f"\nCzas: {czas:.2f}s  (oczekiwany ≈ 3s: 1+1+1, ostatni krok równolegle)")


asyncio.run(main())
