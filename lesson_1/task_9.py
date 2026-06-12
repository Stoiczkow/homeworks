'''
Prosty kalkulator:
Utwórz plik task9_calculator.py .
Poproś o dwie liczby i znak ( + , - , * , / ).
Wykonaj operację i wyświetl wynik.
Użyj if/elif/else
'''

a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
dzialanie = input("Podaj działanie (+, -, *, /): ")

if dzialanie == "+":
    wynik = a + b
    print(f"Wynik: {wynik}")
elif dzialanie == "-":
    wynik = a - b
    print(f"Wynik: {wynik}")
elif dzialanie == "*":
    wynik = a * b
    print(f"Wynik: {wynik}")
elif dzialanie == "/":
    if b != 0:
        wynik = a / b
        print(f"Wynik: {wynik}")
    else:
        print("Błąd: nie można dzielić przez zero.")
else:
    print("Nieznane działanie.")
