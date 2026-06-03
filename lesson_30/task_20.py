import random, time
from multiprocessing import Pool

# Zadanie 20 – AI: Równoległe przetwarzanie obrazów (symulacja)
# Załóżmy, że masz do przetworzenia 10 "obrazów", reprezentowanych jako listy 1000x1000
# losowych liczb. Napisz funkcję zastosuj_filtr(obraz), która iteruje po każdym "pikselu" i
# wykonuje na nim jakąś operację matematyczną (np. piksel * 1.1), symulując zadanie CPU-
# bound. Użyj multiprocessing.Pool do przetworzenia wszystkich 10 obrazów równolegle i zmierz
# czas. Porównaj go z czasem wykonania sekwencyjnego

import random
import time
from multiprocessing import Pool

images = [
    [[random.randint(1, 10) for _ in range(1000)] for _ in range(1000)]
    for _ in range(10)
]

def zastosuj_filtr(obraz):
    wynik = []

    for row in obraz:
        new_row = []

        for pixel in row:
            new_row.append(pixel * 1.1)

        wynik.append(new_row)

    return wynik

# multiprocessing
start_mp = time.time()

with Pool(processes=10) as pool:
    images_parallel = pool.map(zastosuj_filtr, images)

end_mp = time.time()

# sekwencyjnie
start_seq = time.time()

images_seq = [zastosuj_filtr(image) for image in images]

end_seq = time.time()

print(f"Czas multiprocessing: {end_mp - start_mp:.2f} s")
print(f"Czas sekwencyjnie: {end_seq - start_seq:.2f} s")