from dataclasses import dataclass

# ✏ Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.

@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int

film_1 = Film("Film_1", "rezyser_1", 2000)
film_2 = Film("Film_2", "rezyser_2", 2010)
print(film_1)
print(film_2)
