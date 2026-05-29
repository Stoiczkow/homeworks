"""
Zadanie 13 – Pula procesów do przetwarzania danych
Sprawdzenie liczb pierwszych dla 100 losowych liczb za pomocą multiprocessing.Pool.
"""
import multiprocessing
import random


def czy_pierwsza(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    liczby = [random.randint(1, 1000) for _ in range(100)]
    print(f"Lista liczb: {liczby}\n")

    with multiprocessing.Pool() as pool:
        wyniki = pool.map(czy_pierwsza, liczby)

    pierwsze = [l for l, pierwsza in zip(liczby, wyniki) if pierwsza]
    print(f"Liczby pierwsze ({len(pierwsze)}): {pierwsze}")
