# Zadanie 4 – Czytelny Punkt
# Stwórz klasę Punkt do reprezentowania punktu w 2D, z atrybutami x i y. Zaimplementuj metodę str, aby print(punkt) wyświetlał współrzędne w formacie (x, y).

class Punkt:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"
    
punkt_1 = Punkt(10, 3)

print(punkt_1)
