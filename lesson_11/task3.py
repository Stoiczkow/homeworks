# Zadanie 3 – Dziedziczenie Pracownik -> Programista
# Stwórz klasę bazową Pracownik z atrybutami imie i stawka_godzinowa. Dodaj metodę oblicz_pensje(liczba_godzin). Następnie stwórz klasę potomną Programista, która dziedziczy po Pracownik. W klasie Programista dodaj atrybut jezyki_programowania (lista stringów). Stwórz obiekt klasy Programista i wywołaj na nim metodę oblicz_pensje.

class Pracownik:
    def __init__(self, imie, stawka_godzinowa):
        self.imie = imie
        self.stawka_godzinowa = stawka_godzinowa
    def oblicz_pensje(self, liczba_godzin):
        pensja = self.stawka_godzinowa * liczba_godzin
        return pensja

class Programista(Pracownik):
    def __init__(self, imie, stawka_godzinowa, jezyki_programowania):
        super().__init__(imie, stawka_godzinowa)
        self.jezyki_programowania = jezyki_programowania

pracownik_1 = Programista("Daniel", 50, ["Python", "Java"])

print(pracownik_1.oblicz_pensje(160))

print(pracownik_1)
     



