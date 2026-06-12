'''
Komentowanie kodu: Poniżej znajduje się fragment kodu. Dodaj do niego komentarze
jednoliniowe oraz docstring dla funkcji, wyjaśniając, co robi każda część.
def oblicz_pole_prostokata(a, b):
# Tutaj dodaj docstring
# Tutaj dodaj komentarz
pole = a * b
# Tutaj dodaj komentarz
return pole
bok_a = 10
bok_b = 20
wynik = oblicz_pole_prostokata(bok_a, bok_b)
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")
'''


def oblicz_pole_prostokata(a, b):
    """
    Funkcja oblicza pole prostokąta na podstawie długości boków a i b.
    Zwraca wartość pola jako liczbę.
    """
    # Mnożymy długości boków, aby uzyskać pole
    pole = a * b

    # Zwracamy wynik do miejsca wywołania funkcji
    return pole


# Definicja boków prostokąta
bok_a = 10
bok_b = 20

# Wywołanie funkcji i zapisanie wyniku
wynik = oblicz_pole_prostokata(bok_a, bok_b)

# Wyświetlenie sformatowanego wyniku
print(f"Pole prostokąta o bokach {bok_a} i {bok_b} wynosi {wynik}.")

