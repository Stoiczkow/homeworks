# Zadanie 2 – Atrybuty Produkt
# Zdefiniuj klasę Produkt z konstruktorem init przyjmującym nazwa, cena i kategoria. Stwórz obiekt tej klasy, a następnie wydrukuj każdy z jego atrybutów w osobnej linii.

class Produkt:
    def __init__(self, nazwa, cena, kategoria):
        self.nazwa = nazwa
        self.cena = cena
        self.kategoria = kategoria

produkt_1 = Produkt("Chleb", 3.99, "Pieczywo")

print(produkt_1.nazwa)
print(produkt_1.cena)
print(produkt_1.kategoria)



