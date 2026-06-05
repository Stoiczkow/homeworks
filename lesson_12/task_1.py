''' 
    Zadanie 1 -Klasa danych Film

    Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
    reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je
'''

from dataclasses import dataclass


@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int

film_1 = Film("Ziemia obiecana", "Andrzej Wajda", 1975)
film_2 = Film("Nóż w wodzie", "Roman Polański", 1961)

print(film_1)
print(film_2)