# Zadanie 7 – Proces z argumentem
# Stwórz funkcję potega(liczba, pot). Uruchom ją w nowym procesie, przekazując liczba=5 i
# pot=3. Proces powinien wydrukować wynik.

import multiprocessing

def potega(liczba, pot):
    print(liczba**pot)

if __name__ == '__main__':
    proccess = multiprocessing.Process(target=potega, args=(5,3))

    proccess.start()
    proccess.join()