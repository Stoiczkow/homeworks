# Zadanie 13 – Pula procesów do przetwarzania danych
# Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli
# procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map
# powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś

import random
from multiprocessing import Pool
from sympy import isprime

my_list = []

for i in range(0, 100):
    my_list.append(random.randint(1, 1000))

def checking(num):
    return isprime(num)

if __name__ == "__main__":

    with Pool(processes=4) as pool:
        result = pool.map(checking, my_list)

    print(f"Znaleziono: {result.count(True)} liczb pierwszych")