"""
Stwórz funkcję potega(liczba, pot). Uruchom ją w nowym procesie,
przekazując liczba=5 i pot=3. Proces powinien wydrukować wynik.
"""

import multiprocessing


def potega(liczba, pot):
    wynik = liczba ** pot
    print(f"Wynik {liczba}^{pot} = {wynik}")


if __name__ == '__main__':
    proces = multiprocessing.Process(target=potega, args=(5,3))
    proces.start()
    proces.join()