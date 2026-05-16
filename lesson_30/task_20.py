# Zadanie 20 – AI: Równoległe przetwarzanie obrazów (symulacja)

# Załóżmy, że masz do przetworzenia 10 "obrazów", reprezentowanych jako listy 1000x1000 losowych liczb. Napisz funkcję zastosuj_filtr(obraz), która iteruje po każdym "pikselu" i wykonuje na nim jakąś operację matematyczną (np. piksel * 1.1), symulując zadanie CPU- bound. Użyj multiprocessing.Pool do przetworzenia wszystkich 10 obrazów równolegle i zmierz czas. Porównaj go z czasem wykonania sekwencyjnego.

import random
import time
import multiprocessing


# --- Tworzenie "obrazów" 1000x1000 ---
def generuj_obraz(size=1000):
    return [[random.random() for _ in range(size)] for _ in range(size)]



def zastosuj_filtr(obraz):
    # symulacja ciężkiej operacji CPU
    return [
        [piksel * 1.1 for piksel in wiersz]
        for wiersz in obraz
    ]


# Wersja sekwencyjna
def sekwencyjnie(obrazy):
    start = time.time()
    wyniki = []

    for obraz in obrazy:
        wyniki.append(zastosuj_filtr(obraz))

    end = time.time()
    return end - start


# Wersja równoległa (multiprocessing)
def rownolegle(obrazy):
    start = time.time()

    with multiprocessing.Pool() as pool:
        wyniki = pool.map(zastosuj_filtr, obrazy)

    end = time.time()
    return end - start


def main():
    print("Generowanie obrazów...")
    obrazy = [generuj_obraz(300) for _ in range(10)]  
    # 300 zamiast 1000 dla bezpieczeństwa pamięci i szybkości demo

    print("Start sekwencyjnie...")
    czas_seq = sekwencyjnie(obrazy)
    print(f"Czas sekwencyjny: {czas_seq:.2f} s")

    print("Start równolegle...")
    czas_par = rownolegle(obrazy)
    print(f"Czas równoległy: {czas_par:.2f} s")

    print(f"\nPrzyspieszenie: {czas_seq / czas_par:.2f}x")


if __name__ == "__main__":
    main()