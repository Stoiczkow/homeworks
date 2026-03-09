# 1. ✏ Zadanie 1 – Klasa danych Film
# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je.

from dataclasses import dataclass


@dataclass
class Film:
    title: str
    director: str
    release_year: int


film_1 = Film("LOTR", "John Wick", 1991)
film_2 = Film("Terminator", "James Cameron", 1984)


print(film_1)
print(film_2)
print(film_1 == film_2)