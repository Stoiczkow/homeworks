"""
Zadanie 10 – Metaklasa walidująca
Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
niepoprawnie udokumentowanymi metodami.
"""

class MetaWalidujMetody(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if callable(value) and not key.startswith("__"):
                if not value.__doc__:
                    raise TypeError(f"Method '{key}' must have a docstring")
        return super().__new__(cls, name, bases, dct)


class CorrectClass(metaclass=MetaWalidujMetody):
    def method_1(self):
        """Correct docstring"""
        print("Method 1 works")

    def method_2(self):
        """Correct docstring"""
        print("Method 2 works")


try:
    class IncorrectClass(metaclass=MetaWalidujMetody):
        def good_method_1(self):
            """Good docstring"""
            print("Method 1 works")

        def wrong_method_2(self):
            print("Method 2 works")

except TypeError as e:
    print(f"Error: {e}")

obj_1 = CorrectClass()
obj_1.method_1()
obj_1.method_2()