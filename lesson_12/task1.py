# Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string), reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je
from dataclasses import dataclass

@dataclass
class Film:
    tytul: str
    rezyseria: str
    rok_produkcji: int

film_1 = Film("Spider-Man: Into the Spider-Verse", "Bob Persichettim, Peter Ramsey, Rodney Rothman", 2018)
film_2 = Film("Spider-Man: Across the Spider-Verse", "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson", 2023)

print(film_1)
print(film_2)
