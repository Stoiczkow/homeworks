# Zadanie 12 – GIL w praktyce (CPU-bound)
# Napisz funkcję, która wykonuje intensywne obliczenia, np. sum(i*i for i in
# range(20_000_000)). Zmierz czas wykonania tej funkcji dwa razy pod rząd. Następnie
# zmierz czas wykonania jej dwa razy jednocześnie w dwóch różnych wątkach. Na koniec
# zmierz czas, wykonując ją dwa razy jednocześnie w dwóch różnych procesach. Porównaj i
# wyjaśnij wyniki w komentarzu w kodzie

import time
import threading
from multiprocessing import Process

def heavy_func():
    for i in range(0, 20_000_000):
        num = i * i * i * i * i * i

start_time = time.time()
heavy_func()
end_time = time.time()
print(f"Funkcja zakończyła działanie po {end_time - start_time}")

start_time = time.time()
heavy_func()
end_time = time.time()
print(f"Funkcja zakończyła działanie po {end_time - start_time}")

# Rezultat na moim komputerze:
# Funkcja zakończyła działanie po 2.476755380630493
# Funkcja zakończyła działanie po 2.454252004623413

# Wynik dodajemy do siebie, bo 1 funkcja działała w jednym momencie.
# A więc wykonanie zadań trwało ~ 4,92s

def heavy_func_thread(number):
    start_time = time.time()
    heavy_func()
    end_time = time.time()
    print(f"Funkcja {number} zakończyła działanie po {end_time - start_time}")

func1 = threading.Thread(target=heavy_func_thread, args=(1, ))
func2 = threading.Thread(target=heavy_func_thread, args=(2, ))

func1.start()
func2.start()

func1.join()
func2.join()

# Funkcja 1 zakończyła działanie po 4.780149459838867
# Funkcja 2 zakończyła działanie po 4.804300785064697
# Funkcje działały symultanicznie, a więc wykonanie obu zadań trwało tyle,
# ile zanotowano w drugim princie, tj. ~ 4.80s

def heavy_func_proc(number):
    start_time = time.time()
    heavy_func()
    end_time = time.time()
    print(f"Proces {number} zakończył działanie po {end_time - start_time}")

if __name__ == "__main__":
    
    proc1 = Process(target=heavy_func_proc, args=(1, ))
    proc2 = Process(target=heavy_func_proc, args=(2, ))

    proc1.start()
    proc2.start()

    proc1.join()
    proc2.join()

# Proces 1 zakończył działanie po 2.4404890537261963
# Proces 2 zakończył działanie po 2.4591777324676514
# Procesy działały symultanicznie na dwóch wątkach procesora
# dzięki czemu oba zadania zakończyły się po ~2.45 s pracy