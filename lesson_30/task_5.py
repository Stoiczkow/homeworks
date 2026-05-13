# Zadanie 5 – Naprawa wyścigu
# Zmodyfikuj program z zadania 4, dodając threading.Lock, aby operacja dodawania do listy
# była bezpieczna. Sprawdź, czy teraz długość listy jest zawsze poprawna.

import threading

# Globalna lista
lista = []

lock = threading.Lock()

def dodaj_jedynki():
    for _ in range(100_000):
        with lock:
            lista.append(1)

def dodaj_dwojki():
    for _ in range(100_000):
        with lock:
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