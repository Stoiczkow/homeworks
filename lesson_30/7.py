# Zadanie 7 – Proces z argumentem
# Stwórz funkcję potega(liczba, pot). Uruchom ją w nowym procesie, przekazując liczba=5 i
# pot=3. Proces powinien wydrukować wynik

import multiprocessing
import math

def potega(liczba, pot):
    print(liczba**pot)

if __name__ == "__main__":
    process = multiprocessing.Process(target=potega, args=(5, 3))
    process.start()
    process.join()