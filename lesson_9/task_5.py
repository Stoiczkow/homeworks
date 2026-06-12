"""
Eksport do CSV:
Masz listę słowników z produktami.
Zapisz je do pliku produkty.csv, gdzie pierwszy wiersz to nagłówki.
"""

import csv

produkty = [
    {"nazwa": "Mleko", "cena": 3.50},
    {"nazwa": "Chleb", "cena": 4.20}
]

with open("produkty.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["nazwa", "cena"])
    writer.writeheader()
    writer.writerows(produkty)
