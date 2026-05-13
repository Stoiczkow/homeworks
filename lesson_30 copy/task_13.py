# Zadanie 13 – Pula procesów do przetwarzania danych
# Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli
# procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map
# powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś.


import multiprocessing
import random
from multiprocessing import Pool


def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False 
    return True

if __name__ == '__main__':

    liczby = [random.randint(1, 1000) for _ in range(100)]

    with Pool() as pool:
        results = pool.map(is_prime, liczby)

    primes = sum(results)

    print(f"Ilość liczb pierwszych to: {primes}")