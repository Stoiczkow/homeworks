# 10. 🧠 Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami
import inspect

class MetaWalidujMetody(type):
    def __new__(cls, name, bases, dct):
        for attr_name, attr_value in dct.items():
            if attr_name.startswith("__"):
                continue
            if inspect.isfunction(attr_value):
                if not inspect.getdoc(attr_value):
                    raise TypeError(
                        f"Metoda{attr_name} w klasie {name} wymaga dokumentacji."
                    )
                
        return super().__new__(cls, name, bases, dct)

class DobraKlasa(metaclass=MetaWalidujMetody):
    def metoda_liczba(self):
        """Zwraca liczbe"""
        return 5

    def metoda_hello(self):
        """Wypisuje na ekran hello"""
        print("hello")
    
class ZłaKlasa(metaclass=MetaWalidujMetody):
    def metoda_liczba(self):
        return 5

    def metoda_hello(self):
        print("hello")