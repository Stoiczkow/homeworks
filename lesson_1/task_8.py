'''
Sprawdzanie parzystości:
Utwórz plik task8_even_odd.py
Poproś o liczbę całkowitą i sprawdź, czy jest parzysta.
Wskazówka: operator % 2 
'''

liczba = int(input("Podaj liczbę całkowitą: "))

if liczba % 2 == 0:
    print(f"Liczba {liczba} jest parzysta.")
else:
    print(f"Liczba {liczba} jest nieparzysta.")
