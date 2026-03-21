# adanie 1 – Klasa Film
# Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa obiekty tej klasy i wydrukuj informacje o nich.

class Movies:
    def __init__(self, title, director, prod_year):
        self.title = title
        self.director = director
        self.prod_year = prod_year
    
    def info(self):
        return f'"{self.title}" ({self.prod_year}), reżyseria: {self.director}.'
    
movie_1 = Movies("Spider-Man: Into the Spider-Verse", "Bob Persichettim, Peter Ramsey, Rodney Rothman", 2018)

movie_2 = Movies("Spider-Man: Across the Spider-Verse", "Joaquim Dos Santos, Kemp Powers, Justin K. Thompson", 2023)


print(movie_1.info())
print(movie_2.info())

