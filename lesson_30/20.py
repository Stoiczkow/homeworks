# Zadanie 20 – AI: Równoległe przetwarzanie obrazów (symulacja)
# Załóżmy, że masz do przetworzenia 10 "obrazów", reprezentowanych jako listy 1000x1000
# losowych liczb. Napisz funkcję zastosuj_filtr(obraz), która iteruje po każdym "pikselu" i
# wykonuje na nim jakąś operację matematyczną (np. piksel * 1.1), symulując zadanie CPUbound. Użyj multiprocessing.Pool do przetworzenia wszystkich 10 obrazów równolegle i zmierz
# czas. Porównaj go z czasem wykonania sekwencyjnego.

import random
import time
from multiprocessing import Pool

obrazy = []

def create_image():
    img = []
    for _ in range(1_000_000):
        img.append(random.randint(0,100))
    return img

for _ in range(10):
    obrazy.append(create_image())

def zastosuj_filtr(obraz):
    new_pixels = []
    for pixel in obraz:
        new_pixel = pixel * 1.1 * 1.2 * 1.3 * 1.4 * 1.5
        new_pixels.append(new_pixel)
    return new_pixels

# Sekwencyjnie

# total_time = 0

# for i in range(10):
#     start_time = time.time()
#     zastosuj_filtr(obrazy[i])
#     end_time = time.time()
#     total_time += end_time - start_time

# print(f"Sekwencyjnie zajęło: {total_time}")

# Sekwencyjnie zajęło: 0.8776535987854004

if __name__ == "__main__":
    pool_start = time.time()
    with Pool(processes=8) as pool:
        task = pool.map(zastosuj_filtr, obrazy)


    pool_end = time.time()
    total_time_pool = pool_end - pool_start
    print(total_time_pool)
    print(len(task))

# Czas wykonywania na 8 procesach: 3.0882601737976074
# Czyli na zadaniach CPUbound multiprocessing jest mniej wydajny, gdy operujemy na wielu obiektach