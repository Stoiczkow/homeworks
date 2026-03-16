# Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.

from dataclasses import dataclass


class BrakSrodkowError(Exception):
    pass

# Definicja z PDF
# Klasa danych to zwykła klasa, której głównym celem jest przechowywanie danych (stanu).
# Dekorator @dataclass z modułu dataclasses automatycznie generuje za nas standardowe
# metody, takie jak init(), repr(), eq() i inne.

@dataclass
class KontoBankowe:
    _saldo: float

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna.")

        self._saldo += kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wypłaty nie może być ujemna.")

        if kwota > self._saldo:
            raise BrakSrodkowError("Niewystarczające środki na koncie.")

        self._saldo -= kwota


try:
    konto = KontoBankowe(100)

    print("Saldo początkowe:", konto.saldo)

    konto.wplac(50)
    print("Po wpłacie:", konto.saldo)

    konto.wyplac(30)
    print("Po wyplacie:", konto.saldo)

    konto.wplac(-10)

except ValueError as e:
    print("Błąd wartości:", e)

except BrakSrodkowError as e:
    print("Błąd środków:", e)