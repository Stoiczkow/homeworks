# Stwórz klasę danych (@dataclass) o nazwie Film, która będzie przechowywać tytuł (string),
# reżysera (string) i rok_produkcji (integer). Utwórz dwie instancje tej klasy i wyświetl je

from dataclasses import dataclass

@dataclass
class Film:
    title: str
    director: str
    year: int

shrek = Film("Shrek", "Andrew Adamson, Vicky Jenson", 2001)
toy_story = Film("Toy Story", "John Lasseter", 1995)

print(shrek)
print(toy_story)