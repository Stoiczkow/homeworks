"""
Napisz program, który sumuje liczby w dużej liście (np. 10 milionów elementów).
Podziel listę na 4 części i każdą część zsumuj w osobnym wątku.
Wyniki częściowe dodawaj do globalnej zmiennej suma_calkowita,
zabezpieczając dostęp do niej za pomocą threading.Lock.
"""

import threading

dane = list(range(1, 10_000_001))

suma_calkowita = 0
lock = threading.Lock()

def sumuj_fragment(fragment):
    global suma_calkowita
    lokalna_suma = sum(fragment)

    with lock:
        suma_calkowita += lokalna_suma

krok = len(dane) // 4
fragmenty = [
    dane[0:krok],
    dane[krok:2*krok],
    dane[2*krok:3*krok],
    dane[3*krok:]
]

watki = []

for fragment in fragmenty:
    t = threading.Thread(target=sumuj_fragment, args=(fragment,))
    watki.append(t)
    t.start()

for t in watki:
    t.join()

print("Suma całkowita:", suma_calkowita)
print("Suma wzorcowa (sprawdzająca):", sum(dane))
