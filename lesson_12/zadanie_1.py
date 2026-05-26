from dataclasses import dataclass


@dataclass
class Film:
    tytul: str
    rezyser: str
    rok_produkcji: int


film1 = Film("Inception", "Christopher Nolan", 2010)
film2 = Film("The Godfather", "Francis Ford Coppola", 1972)

print(film1)
print(film2)
