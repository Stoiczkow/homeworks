from dataclasses import dataclass

@dataclass
class Film:
    title: str
    director: str
    production_year: int

film_1 = Film("Inception", "Christopher Nolan", 2010)
film_2 = Film("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999)

print(film_1)
print(film_2)