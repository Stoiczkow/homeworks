# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami.

class MetaWalidujMetody(type):
    def __new__(cls, name, bases, dct):
        for key, value in dct.items():
            if key.endswith("__") and key.startswith("__"):
                pass
            else:
                if not value.__doc__:
                    raise TypeError(f"Method {value} must have docstring")

        return super().__new__(cls, name, bases, dct)
    
class ClassWithDocStrings(metaclass=MetaWalidujMetody):

    def add(self, a, b):
        '''
        adding
        '''
        return a + b

    def multiply(self, a, b):
        '''
        multiplying
        '''
        return a * b
    
test1 = ClassWithDocStrings() # works fine
print(f"Result: {test1.add(5, 5)}\n\n")

class ClassWithoutDocStrings(metaclass=MetaWalidujMetody):

    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

test2 = ClassWithoutDocStrings() # will rise an error