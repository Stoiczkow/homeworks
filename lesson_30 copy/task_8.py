# Zadanie 8 – Komunikacja z procesem
# Stwórz proces, który prosi użytkownika o podanie imienia (input()), a następnie wysyła to
# imię do procesu nadrzędnego za pomocą multiprocessing.Queue. Proces nadrzędny
# odbiera imię i drukuje "Witaj, [imię]!".

from multiprocessing import Process, Queue

def podaj_imie(kolejka, imie):
    kolejka.put(imie)


if __name__ == "__main__":
    imie = input("Podaj imię: ")
    q = Queue()

    p = Process(target=podaj_imie, args=(q, imie))

    p.start()

    imie_uzytkownika = q.get()

    p.join()

    print(f"Witaj, {imie_uzytkownika}!")