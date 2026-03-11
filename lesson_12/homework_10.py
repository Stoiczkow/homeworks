# Zadanie 10 – Metaklasa walidująca
# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i niepoprawnie udokumentowanymi metodami



class MetaWalidujMetody(type):
    def __new__(cls, name, bases, dct):

        # przejście po wszytkich elementach klasy w postaci słownika
        for name2, value in dct.items():
            # Pomijamy metody magiczne, prywatne
            if name2.startswith("__"):
                continue
        
            # Sprawdzamy czy atrybut jest metodą
            if callable(value):
                if value.__doc__ is None or value.__doc__.strip() == "":
                    raise TypeError(
                        f"Metoda '{name2}' w klasie '{name}' musi posiadać docstring."
                    )

        return super().__new__(cls, name, bases, dct)
    

class PoprawnaKlasa(metaclass=MetaWalidujMetody):
    
    nie_metoda = 6

    def metoda1(self):
        """Przykładowa metoda."""
        print("Metoda 1")

    def metoda2(self):
        """Druga metoda."""
        print("Metoda 2")

pk = PoprawnaKlasa()


try:
    class ZlaKlasa(metaclass=MetaWalidujMetody):
        
        nie_metoda = 6

        def metoda1(self):
            print("Metoda 1")

        def metoda2(self):
            """Druga metoda."""
            print("Metoda 2")
except TypeError as e:
    print(e)

# zk = ZlaKlasa()

