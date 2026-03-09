# Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string), reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je

from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int

scify = Film("Terminator", "Cameron", "1984")

animacja = Film("Spider-Man", "Kamp", "2023")

print(scify)
print(animacja)
