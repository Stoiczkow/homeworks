"""
Licznik słów:
Program pyta o nazwę pliku, odczytuje go i zlicza liczbę słów.
Obsługuje FileNotFoundError, jeśli plik nie istnieje.
"""

nazwa = input("Podaj nazwę pliku: ")

try:
    with open(nazwa, "r", encoding="utf-8") as f:
        zawartosc = f.read()
        slowa = zawartosc.split()
        print("Liczba słów w pliku:", len(slowa))

except FileNotFoundError:
    print("Błąd: plik nie istnieje.")
