# Zadanie 10 – Metaklasa walidująca

# Stwórz metaklasę MetaWalidujMetody, która podczas tworzenia nowej klasy sprawdza, czy
# wszystkie jej metody (poza metodami "magicznymi", czyli zaczynającymi się od __) mają
# docstring. Jeśli któraś metoda go nie ma, metaklasa powinna podnieść TypeError z
# informacją, która metoda wymaga dokumentacji. Przetestuj ją, tworząc klasę z poprawnie i
# niepoprawnie udokumentowanymi metodami
# bases → klasy bazowe (np. [object])
# attrs → słownik wszystkiego, co jest w klasie: metody, zmienne, właściwości


# Metaklasa to „klasa, która tworzy inne klasy”.
# metaklasa
class MetaWalidujMetody(type):
    def __new__(cls, name, bases, attrs):
        
        # Pętla po wszystkich elementach klasy
        # attrs.items() to wszystkie rzeczy w klasie, np.:
        for name, method in attrs.items():

            # sprawdzamy czy to metoda i nie jest magiczna
            if callable(method) and not name.startswith("__"):

                # sprawdzamy czy ma docstring
                if method.__doc__ is None:
                    raise TypeError(f"Metoda '{name}' musi mieć docstring")
                
        # 5️⃣ Utworzenie klasy
        return super().__new__(cls, name, bases, attrs)


# poprawna klasa
class PoprawnaKlasa(metaclass=MetaWalidujMetody):
    
    def metoda1(self):
        """Opis metody 1"""
        print("Metoda 1 działa")

    def metoda2(self):
        """Opis metody 2"""
        print("Metoda 2 działa")


# test błędnej klasy
try:
    class ZlaKlasa(metaclass=MetaWalidujMetody):

        def metoda1(self):
            print("OK")

        def metoda2(self):
            print("Brak opisu")

except TypeError as e:
    print("Błąd:", e)


# test poprawnej klasy
obiekt = PoprawnaKlasa()
obiekt.metoda1()
obiekt.metoda2()

# # Metaklasa sprawdza każdą metodę w momencie tworzenia klasy
# Wszystkie zwykłe metody mają docstring
# Jeśli jakaś metoda nie ma docstringa → TypeError, klasa nie zostaje utworzona
# Klasy z poprawnymi docstringami działają normalnie
# try except przychwytuje błąd i program działa dalej