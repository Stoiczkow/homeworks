'''
Wektor 2D i przeciążanie operatorów
Stwórz klasę Wektor2D z atrybutami x i y. Przeciąż następujące operatory:
__add__(self, other) : do dodawania dwóch wektorów (dodajemy odpowiadające
sobie współrzędne).
__sub__(self, other) : do odejmowania wektorów.
eq(self, other): do porównywania, czy dwa wektory są równe (mają te same x i y).
Dodatkowo zaimplementuj str do ładnego wyświetlania. Przetestuj działanie, tworząc
dwa wektory i wykonując na nich wszystkie zaimplementowane operacje. 
'''

class Wektor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Wektor2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Wektor2D(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"({self.x}, {self.y})"


w1 = Wektor2D(3, 5)
w2 = Wektor2D(1, 2)

print(w1 + w2)
print(w1 - w2)
print(w1 == w2)
