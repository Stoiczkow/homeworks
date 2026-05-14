#3
import json

konfiguracja = {
    "uzytkownik": "admin",
    "motyw": "ciemny",
    "rozdzielczosc": [1920, 1080]
}

plik = open("config.json", "w", encoding="utf-8")
json.dump(konfiguracja, plik, indent=4, ensure_ascii=False)
plik.close()

print("Plik config.json zostal zapisany.")
#4
import json

plik = open("config.json", "r", encoding="utf-8")
konfiguracja = json.load(plik)
plik.close()

uzytkownik = konfiguracja["uzytkownik"]
motyw = konfiguracja["motyw"]

print("Witaj, " + uzytkownik + "! Twoj motyw to " + motyw + ".")
#5
import csv

produkty = [
    {"nazwa": "Mleko", "cena": 3.50},
    {"nazwa": "Chleb", "cena": 4.20}
]

plik = open("produkty.csv", "w", newline="", encoding="utf-8")
writer = csv.DictWriter(plik, fieldnames=["nazwa", "cena"])
writer.writeheader()
writer.writerows(produkty)
plik.close()

print("Plik produkty.csv zostal zapisany.")
#6
import csv

suma = 0.0

plik = open("produkty.csv", "r", encoding="utf-8")
reader = csv.DictReader(plik)

for wiersz in reader:
    suma = suma + float(wiersz["cena"])

plik.close()

print("Suma cen wszystkich produktow: " + str(suma) + " zl")
#7
import os

os.makedirs("Projekt/src")
os.makedirs("Projekt/data")
os.makedirs("Projekt/docs")

print("Foldery zostaly utworzone.")
#8
szukane_slowo = input("Podaj szukane slowo: ")

plik_wejsciowy = open("log.txt", "r", encoding="utf-8")
plik_wyjsciowy = open("wyniki_wyszukiwania.txt", "w", encoding="utf-8")

for linia in plik_wejsciowy:
    if szukane_slowo in linia:
        plik_wyjsciowy.write(linia)

plik_wejsciowy.close()
plik_wyjsciowy.close()

print("Wyniki zapisano do pliku wyniki_wyszukiwania.txt")
#9
import openpyxl

skoroszyt = openpyxl.Workbook()
arkusz = skoroszyt.active

arkusz["A1"] = "Czynsz"
arkusz["B1"] = 1500

arkusz["A2"] = "Jedzenie"
arkusz["B2"] = 800

arkusz["A3"] = "Transport"
arkusz["B3"] = 300

arkusz["A4"] = "Suma"
arkusz["B4"] = "=SUM(B1:B3)"

skoroszyt.save("finanse.xlsx")

print("Plik finanse.xlsx zostal zapisany.")
#10
