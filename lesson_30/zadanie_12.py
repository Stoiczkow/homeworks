"""
Zadanie 12 – GIL w praktyce (CPU-bound)

Wnioski (wyjaśnienie w komentarzu):
- Sekwencyjnie: ~T sekund (bazowy czas)
- Dwa wątki:    ~T sekund (tak samo!) – GIL pozwala wykonywać tylko jeden wątek
                Python naraz, więc CPU-bound zadania NIE korzystają z wątków
- Dwa procesy:  ~T/2 sekund – każdy proces ma własny interpreter i własny GIL,
                dzięki czemu oba rdzenie CPU pracują jednocześnie
"""
import multiprocessing
import threading
import time


def oblicz():
    return sum(i * i for i in range(20_000_000))


# ── Sekwencyjnie ─────────────────────────────────────────────────────────────
start = time.perf_counter()
oblicz()
oblicz()
czas_sekwencyjny = time.perf_counter() - start
print(f"Sekwencyjnie:  {czas_sekwencyjny:.3f}s")


# ── Dwa wątki ────────────────────────────────────────────────────────────────
t1 = threading.Thread(target=oblicz)
t2 = threading.Thread(target=oblicz)

start = time.perf_counter()
t1.start()
t2.start()
t1.join()
t2.join()
czas_watki = time.perf_counter() - start
print(f"Dwa wątki:     {czas_watki:.3f}s  (GIL – brak przyspieszenia dla CPU-bound)")


# ── Dwa procesy ──────────────────────────────────────────────────────────────
if __name__ == '__main__':
    p1 = multiprocessing.Process(target=oblicz)
    p2 = multiprocessing.Process(target=oblicz)

    start = time.perf_counter()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    czas_procesy = time.perf_counter() - start
    print(f"Dwa procesy:   {czas_procesy:.3f}s  (brak GIL – prawdziwa równoległość)")

    print(f"\nPrzyspieszenie procesów vs sekwencyjnie: {czas_sekwencyjny / czas_procesy:.2f}x")
