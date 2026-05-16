# Zadanie 13 – Pula procesów do przetwarzania danych

# Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś.

import random
import multiprocessing
import math


# Funkcja sprawdzająca, czy liczba jest pierwsza
def czy_pierwsza(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":

    # 100 losowych liczb
    liczby = [random.randint(1, 1000) for _ in range(100)]

    print("Wylosowane liczby:")
    print(liczby)

    # pula procesów
    with multiprocessing.Pool() as pool:

      
        wyniki = pool.map(czy_pierwsza, liczby)

    # Zliczanie liczb pierwszych
    ile_pierwszych = sum(wyniki)

    print("\nWyniki True/False:")
    print(wyniki)

    print(f"\nZnaleziono {ile_pierwszych} liczb pierwszych.")