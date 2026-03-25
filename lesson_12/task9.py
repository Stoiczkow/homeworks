# Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.
from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass
@dataclass
class KontoBankowe:
    _saldo: float

    @property
    def saldo(self):
        return self._saldo
    
    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota nie może być ujemna")            
        self._saldo += kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota nie może być ujemna")
        elif self._saldo < kwota:
            raise BrakSrodkowError("Brak środków do wypłaty.")
        self._saldo -= kwota

try:
    user_1 = KontoBankowe(100)
    user_1.wplac(-100)
except ValueError as e:
    print(f"Błąd: {e}")
except BrakSrodkowError as f:
    print(f"Błąd: {f}")
else:
    print(user_1.saldo)
try:
    user_2 = KontoBankowe(100)
    user_2.wyplac(101)
except ValueError as e:
    print(f"Błąd: {e}")
except BrakSrodkowError as f:
    print(f"Błąd: {f}")   
else:
    print(user_2.saldo)

try:
    user_3 = KontoBankowe(100)
    user_3.wyplac(100)
except ValueError as e:
    print(f"Błąd: {e}")
except BrakSrodkowError as f:
    print(f"Błąd: {f}")
else:
    print(user_3.saldo)