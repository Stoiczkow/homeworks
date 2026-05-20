import asyncio
import time


async def opoznione_zadanie(nazwa: str, czas: int) -> str:
    print(f"[{nazwa}] start (opóźnienie {czas}s)")
    await asyncio.sleep(czas)
    print(f"[{nazwa}] koniec")
    return f"wynik {nazwa}"


async def main() -> None:
    start = time.time()
    wyniki = await asyncio.gather(
        opoznione_zadanie("Zad1", 1),
        opoznione_zadanie("Zad2", 4),
        opoznione_zadanie("Zad3", 2),
    )
    print(f"\nWyniki: {wyniki}")
    print(f"Całkowity czas: {time.time() - start:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())