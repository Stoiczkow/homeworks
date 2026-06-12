'''
Stwórz klasę Film, która przy tworzeniu obiektu będzie przyjmować tytul, rezyser i
rok_produkcji. Dodaj metodę informacje(), która będzie zwracać string z pełnymi
informacjami o filmie w formacie: "Tytuł" (rok_produkcji), reżyseria: Reżyser. Stwórz dwa
obiekty tej klasy i wydrukuj informacje o nich.
'''

class Film:
    def __init__(self, tytul, rezyser, rok_produkcji):
        self.tytul = tytul
        self.rezyser = rezyser
        self.rok_produkcji = rok_produkcji

    def informacje(self):
        return f"\"{self.tytul}\" ({self.rok_produkcji}), reżyseria: {self.rezyser}"


film1 = Film("Incepcja", "Christopher Nolan", 2010)
film2 = Film("Matrix", "Wachowscy", 1999)

print(film1.informacje())
print(film2.informacje())
