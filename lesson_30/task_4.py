# Zadanie 4 – Problem wyścigu
# Napisz program z globalną listą. Stwórz 2 wątki - jeden dodaje do listy 100 tysięcy razy
# liczbę 1, a drugi 100 tysięcy razy liczbę 2. Po zakończeniu obu wątków, sprawdź długość
# listy. Czy wynosi ona 200 tysięcy? Uruchom program kilka razy.

import threading

# Globalna lista
lista = []

def dodaj_jedynki():
    for _ in range(100_000):
        lista.append(1)

def dodaj_dwojki():
    for _ in range(100_000):
        lista.append(2)

# Tworzenie wątków
w1 = threading.Thread(target=dodaj_jedynki)
w2 = threading.Thread(target=dodaj_dwojki)

# Start wątków
w1.start()
w2.start()

# Oczekiwanie na zakończenie
w1.join()
w2.join()

# Wynik
print("Długość listy:", len(lista))