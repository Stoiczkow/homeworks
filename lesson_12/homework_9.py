# Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.

from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass


@dataclass
class KontoBankowe():
    _saldo: int

    @property
    def saldo(self):
        return self._saldo


    def wplac(self, kwota: int):
        if kwota < 0:
            raise ValueError("Nie wpłacisz minusowej kwoty")

        self._saldo += kwota

    def wyplac(self, kwota: int):
        if kwota < 0:
            raise ValueError("Nie wypłacisz minusowej kwoty")
        
        if kwota > self._saldo:
            raise BrakSrodkowError("Brak środków na koncie.")

        self._saldo -= kwota

try:
    k = KontoBankowe(0)

    # k.wplac(-5)
    # print(k.saldo)
    k.wplac(500)
    print(k.saldo)
    # k.wyplac(-7)
    # print(k.saldo)
    k.wyplac(200)
    print(k.saldo)
    k.wyplac(700)
    print(k.saldo)
except ValueError as e:
    print("Klingonie zła kwota")
except BrakSrodkowError as e:
    print(e)





