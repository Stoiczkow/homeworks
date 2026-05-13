# Zadanie 13 – Pula procesów do przetwarzania danych
# Stwórz listę 100 losowych liczb od 1 do 1000. Użyj multiprocessing.Pool do stworzenia puli procesów, która dla każdej liczby sprawdzi, czy jest ona liczbą pierwszą. Funkcja pool.map powinna zwrócić listę wartości True/False. Wydrukuj, ile liczb pierwszych znalazłeś.

import random
from multiprocessing import Pool, pool

def czy_liczba_pierwsza(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":  #zapobiega problemom z multiprocessingiem na Windows w procesach potomnych i chyba ogolenie jest dobra praktyka
    liczby = [random.randint(1, 1000) for _ in range(100)]
    with Pool() as pool:
        wyniki = pool.map(czy_liczba_pierwsza, liczby)
    print(f"Liczby pierwsze: {sum(wyniki)}")    

