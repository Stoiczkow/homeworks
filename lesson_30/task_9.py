# Napisz program, który sumuje liczby w dużej liście (np. 10 milionów elementów). Podziel
# listę na 4 części i każdą część zsumuj w osobnym wątku. Wyniki częściowe dodawaj do
# globalnej zmiennej suma_calkowita, zabezpieczając dostęp do niej za pomocą
# threading.Lock.

import threading

suma_calkowita = 0
lock = threading.Lock()

def sumuj_czesc(czesc_listy):
    """
    Funkcja sumująca liczby w danej części listy i dodająca wynik do globalnej sumy.
    """
    global suma_calkowita
    czestciowa_suma = sum(czesc_listy)
    
    with lock:
        suma_calkowita += czestciowa_suma

def main():
    global suma_calkowita
    
    liczby = list(range(1, 10_000_001))
    
    rozmiar_czesci = len(liczby) // 4
    czesci = [
        liczby[0:rozmiar_czesci],
        liczby[rozmiar_czesci:2*rozmiar_czesci],
        liczby[2*rozmiar_czesci:3*rozmiar_czesci],
        liczby[3*rozmiar_czesci:]
    ]
    
    watki = []
    for czesc in czesci:
        watek = threading.Thread(target=sumuj_czesc, args=(czesc,))
        watki.append(watek)
        watek.start()
    
    for watek in watki:
        watek.join()
    
    print(f"Suma całkowita: {suma_calkowita}")
    
    spodziewana_suma = (10_000_000 * 10_000_001) // 2
    print(f"Spodziewana suma: {spodziewana_suma}")
    print(f"Wynik poprawny: {suma_calkowita == spodziewana_suma}")

if __name__ == "__main__":
    main()

