'''
    Zadanie 7 - Alternatywny konstruktor dla Daty

    Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
    nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
    tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int
'''

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok

    @classmethod
    def ze_stringa(cls, tekst):
        dzien_str, miesiac_str, rok_str = tekst.split("-")
        return cls(int(dzien_str), int(miesiac_str), int(rok_str))

    def __repr__(self):
        return f"Data({self.dzien}, {self.miesiac}, {self.rok})"


data = Data.ze_stringa("05-06-2026")
print(data)
