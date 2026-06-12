"""
Import z CSV:
Program odczytuje plik produkty.csv i oblicza sumę cen wszystkich produktów.
Używa csv.DictReader.
"""

import csv

suma = 0

with open("produkty.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for wiersz in reader:
        suma += float(wiersz["cena"])

print("Suma cen produktów:", suma)
