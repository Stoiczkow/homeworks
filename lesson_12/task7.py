# Tworzenie alternatywnego konstruktora

# Zadanie 7 – Alternatywny konstruktor dla Daty
# Stwórz klasę Data z atrybutami dzien, miesiac, rok. Dodaj metodę klasy (@classmethod) o nazwie ze_stringa, która przyjmuje datę w formacie "DD-MM-RRRR" (np. "25-12-2023") i tworzy na jej podstawie obiekt klasy Data. Pamiętaj o konwersji typów na int.


class Data:
    # atrybuty klasy, konstruktor
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    # metoda klasy dekorator    
    @classmethod        # Dekorator @classmethod oznacza, że metoda: działa na klasie, nie na obiekcie
    # zamiast self przyjmuje cls (czyli klasę)
    # Czyli cls to w tym przypadku Data.


    # przyjmujemy klase cls w argumencie
    def ze_stringa(cls, input: str):
        splitted_input = input.split(sep="-")   # dzielienie tekstu na podstawie sepratora - dd-mm-rr pdzieli strina na 3 kawałki i zwóci listę z 3 elementami 0 -dd , 1-mm, 2 -rr
        return cls(int(splitted_input[0]), int(splitted_input[1]),int(splitted_input[2]))            # wyciągamy z listy
    
    # Wywołanie
    # Tworzymy obiekt za pomoca metody kalsowej

example = Data.ze_stringa("12-10-1004")
print(example.day)

#
# Tu dzieją się trzy rzeczy:
# Pobieramy elementy listy
# Zamieniamy je z string → int
# Wywołujemy konstruktor klasy