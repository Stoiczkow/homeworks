
from dataclasses import dataclass
#8
'''while True:
    try:
        a = float(input("Podaj pierwsza liczbe: "))
        b = float(input("Podaj druga liczbe: "))
        operacja = input("Podaj operacje (+, -, *, /): ")

        if operacja == "+":
            wynik = a + b
        elif operacja == "-":
            wynik = a - b
        elif operacja == "*":
            wynik = a * b
        elif operacja == "/":
            wynik = a / b
        else:
            print("Nieznana operacja.")

    except ValueError:
        print("Blad: podaj poprawna liczbe.")

    except ZeroDivisionError:
        print("Blad: nie moznadzielic przez zero.")

    else:
        print("Wynik: " + str(wynik))

    finally:
        print("Koniec obliczen.")'''
#9
class BrakSrodkowError(Exception):
    pass


@dataclass
class KontoBankowe:
    _saldo: float = 0.0

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wplaty nie moze byc ujemna.")
        self._saldo = self._saldo + kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wyplaty nie moze byc ujemna.")
        if kwota > self._saldo:
            raise BrakSrodkowError("Brak wystarczajacych srodkow na koncie.")
        self._saldo = self._saldo - kwota
#10
class MetaWalidujMetody(type):
    def __new__(mcs, nazwa, rodzice, przestrzen):
        for klucz, wartosc in przestrzen.items():
            if klucz.startswith("__"):
                continue
            if callable(wartosc):
                if not wartosc.__doc__:
                    raise TypeError("Metoda '" + klucz + "' nie ma docstringa.")
        return super().__new__(mcs, nazwa, rodzice, przestrzen)


# Klasa z poprawnie udokumentowanymi metodami
class PoprawnaKlasa(metaclass=MetaWalidujMetody):
    def metoda_a(self):
        """Ta metoda robi cos uzytecznego."""
        pass

    def metoda_b(self):
        """Ta metoda tez ma dokumentacje."""
        pass


print("PoprawnaKlasa utworzona bez bledow.")


# Klasa z brakujacym docstringiem
try:
    class NiepoprawnaKlasa(metaclass=MetaWalidujMetody):
        def metoda_dobra(self):
            """Ta metoda ma docstringa."""
            pass

        def metoda_zla(self):
            pass

except TypeError as e:
    print("Blad przy tworzeniu klasy: " + str(e))