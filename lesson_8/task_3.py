'''
Czytanie pliku: Napisz funkcję, która próbuje otworzyć i odczytać plik o podanej nazwie.
Obsłuż wyjątki FileNotFoundError (gdy pliku nie ma) oraz PermissionError (gdy nie
ma uprawnień do odczytu)
'''

def czytaj_plik(nazwa: str):
    try:
        with open(nazwa, "r", encoding="utf-8") as plik:
            return plik.read()

    except FileNotFoundError:
        print("Błąd: plik nie istnieje.")
    except PermissionError:
        print("Błąd: brak uprawnień do odczytu pliku.")

zawartosc = czytaj_plik("dane.txt")
print(zawartosc)
