'''
Kalkulator pola powierzchni:
Utwórz plik task4_area.py .
Program powinien poprosić o długość i szerokość prostokąta.
Oblicz i wyświetl jego pole powierzchni.
Nie zapomnij o int() lub float()
'''

dlugosc = float(input("Podaj długość prostokąta: "))
szerokosc = float(input("Podaj szerokość prostokąta: "))

pole = dlugosc * szerokosc

print(f"Pole prostokąta wynosi {pole}.")