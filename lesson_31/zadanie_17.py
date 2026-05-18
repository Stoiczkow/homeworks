import asyncio
import time


async def pobierz_id_uzytkownika(nazwa_uzytkownika: str) -> int:
    print(f"Pobieram ID dla użytkownika '{nazwa_uzytkownika}'...")
    await asyncio.sleep(1)
    return 42


async def pobierz_posty(id_uzytkownika: int) -> list[int]:
    print(f"Pobieram posty dla użytkownika {id_uzytkownika}...")
    await asyncio.sleep(1)
    return [101, 102, 103, 104]


async def pobierz_komentarze(id_postu: int) -> list[str]:
    print(f"Pobieram komentarze dla postu {id_postu}...")
    await asyncio.sleep(1)
    return [f"Komentarz {i} do postu {id_postu}" for i in range(1, 4)]


async def main() -> None:
    start = time.time()

    user_id = await pobierz_id_uzytkownika("jkowalski")
    posty = await pobierz_posty(user_id)
    komentarze = await asyncio.gather(*(pobierz_komentarze(pid) for pid in posty))

    print("\n--- Wyniki ---")
    for pid, kom in zip(posty, komentarze):
        print(f"Post {pid}: {kom}")

    print(f"\nCzas wykonania: {time.time() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
