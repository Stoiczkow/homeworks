'''
Dziedziczenie Pracownik -> Programista
Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę
oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która
dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista
stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje.
'''

class Pracownik:
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa

    def oblicz_pensje(self, liczba_godzin):
        return self.stawka_godzinowa * liczba_godzin


class Programista(Pracownik):
    def __init__(self, imie, stawka_godzinowa, jezyki_programowania):
        super().__init__(imie, stawka_godzinowa)
        self.jezyki_programowania = jezyki_programowania


p = Programista("Ala", 80, ["Python", "JavaScript"])
print(p.oblicz_pensje(160))
