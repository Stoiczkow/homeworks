#  ✏ Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string), reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je

# Importujemy dekorator z bibloteki datacalss

from dataclasses import dataclass

@dataclass  # dekorator     # Pisanie klasy za pomocą dataclass
class Film:     # nazwa klasy       # ten konstruktor nie robi walidacji danych 
    tutul: str      #dekorwanie
    rezyszer: str       # Python olewa czy str czy int
    rok_produkcji: int

# Uwtworzenie instacji klas
scifi = Film("Terminator", "Cameron", "1984")
komdia = Film("chłopaki nie płączą", "Lubaszenko", 1997) # adnotacje w klasie

#Wyświetlenie ich 
print(scifi)

print(komdia)


# domyślnie tak wypluwa Film(tutul='Terminator' - jest  =
