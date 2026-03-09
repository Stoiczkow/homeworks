# 7. 🧠 Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o
# nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i
# tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.

class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    @classmethod
    def convert(cls, data_str: str):
        splitted_data = data_str.split("-")
        return cls(int(splitted_data[0]), int(splitted_data[1]), int(splitted_data[2]))
    
data_1 = Data.convert("09-03-2026")
print(data_1.day)
print(data_1.month)
print(data_1.year)