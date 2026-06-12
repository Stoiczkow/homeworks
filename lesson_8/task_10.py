"""
Mini-projekt: Sumator liczb z pliku

Napisz program, który:
a. Pyta użytkownika o nazwę pliku.
b. Otwiera plik i czyta go linia po linii.
c. Każdą linię próbuje przekonwertować na liczbę i dodać do sumy.
d. Ignoruje linie, których nie da się przekonwertować na liczbę (obsługa ValueError).
e. Obsługuje FileNotFoundError, jeśli plik nie istnieje.
f. Na końcu, w bloku finally, wyświetla obliczoną sumę (nawet jeśli wystąpiły błędy).
"""

suma = 0

nazwa = input("Podaj nazwę pliku: ")

try:
    plik = open(nazwa, "r", encoding="utf-8")

    for linia in plik:
        linia = linia.strip()
        try:
            liczba = float(linia)
            suma += liczba
        except ValueError:
            # Ignorujemy linie, które nie są liczbami
            pass

except FileNotFoundError:
    print("Błąd: podany plik nie istnieje.")

finally:
    # Zamykamy plik tylko jeśli udało się go otworzyć
    try:
        plik.close()
    except NameError:
        pass

    print(f"Suma liczb z pliku: {suma}")
