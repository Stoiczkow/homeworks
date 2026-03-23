# Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.

class Data:
    def __init__(self, dzien, miesiac, rok):
        self.dzien = dzien
        self.miesiac = miesiac
        self.rok = rok
    
    @classmethod

    def ze_stringa(cls, data_str):
        dzien, miesiac, rok = data_str.split("-")
        dzien = int(dzien)
        miesiac = int(miesiac)
        rok = int(rok)
        return cls(dzien, miesiac, rok)
    
nowadata = Data.ze_stringa("10-12-1990")

print(nowadata)
