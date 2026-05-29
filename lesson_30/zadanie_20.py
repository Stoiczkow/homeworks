"""
Zadanie 20 – Równoległe przetwarzanie obrazów (symulacja, CPU-bound)
multiprocessing.Pool przetwarza 10 "obrazów" (macierzy 1000×1000) równolegle.
"""
import multiprocessing
import random
import time


def generuj_obraz():
    return [[random.random() for _ in range(1000)] for _ in range(1000)]


def zastosuj_filtr(obraz):
    return [[piksel * 1.1 for piksel in wiersz] for wiersz in obraz]


if __name__ == '__main__':
    print("Generowanie 10 obrazów 1000×1000...")
    obrazy = [generuj_obraz() for _ in range(10)]

    # ── Sekwencyjnie ──────────────────────────────────────────────────────────
    start = time.perf_counter()
    for obraz in obrazy:
        zastosuj_filtr(obraz)
    czas_sekwencyjny = time.perf_counter() - start
    print(f"Sekwencyjnie:  {czas_sekwencyjny:.2f}s")

    # ── Pool (multiprocessing) ─────────────────────────────────────────────────
    start = time.perf_counter()
    with multiprocessing.Pool() as pool:
        pool.map(zastosuj_filtr, obrazy)
    czas_pool = time.perf_counter() - start
    print(f"Pool procesów: {czas_pool:.2f}s")

    przyspieszenie = czas_sekwencyjny / czas_pool
    print(f"\nPrzyspieszenie: {przyspieszenie:.2f}x  (rdzenie: {multiprocessing.cpu_count()})")
