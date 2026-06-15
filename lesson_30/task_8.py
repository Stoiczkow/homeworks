"""
Stwórz proces, który prosi użytkownika o podanie imienia (input()),
a następnie wysyła to imię do procesu nadrzędnego za pomocą multiprocessing.Queue.
Proces nadrzędny odbiera imię i drukuje "Witaj, [imię]!".
"""

import multiprocessing

def pobierz_imie(kolejka):
    imie = input("Podaj swoje imię: ")
    kolejka.put(imie)

if __name__ == "__main__":
    kolejka = multiprocessing.Queue()

    proces = multiprocessing.Process(target=pobierz_imie, args=(kolejka,))
    proces.start()
    proces.join()

    imie = kolejka.get()
    print(f"Witaj, {imie}!")
