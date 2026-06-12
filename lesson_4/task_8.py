'''
Obliczanie wieku psa: Przyjmuje się, że pierwszy rok życia psa to 15 ludzkich lat, drugi to
9, a każdy kolejny to 5. Napisz program, który pyta o wiek psa w latach, a następnie oblicza
i wyświetla jego wiek w "ludzkich" latach.
'''

wiek_psa = int(input("Podaj wiek psa w latach: "))

if wiek_psa == 1:
    wiek_ludzki = 15
elif wiek_psa == 2:
    wiek_ludzki = 15 + 9
else:
    wiek_ludzki = 15 + 9 + (wiek_psa - 2) * 5

print(f"Wiek psa w ludzkich latach: {wiek_ludzki}")
