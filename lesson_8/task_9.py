"""
Kontekstowy menedżer with:
Pokaż, jak with open(...) upraszcza kod z zadania 3,
eliminując potrzebę jawnego finally.
"""

def czytaj_plik(nazwa):
    try:
        with open(nazwa, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print("Błąd: plik nie istnieje.")
    except PermissionError:
        print("Błąd: brak uprawnień do odczytu pliku.")



print(czytaj_plik("dane.txt"))
