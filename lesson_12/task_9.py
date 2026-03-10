"""
Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
ValueError , jeśli kwota jest ujemna.
Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
BrakSrodkowError , jeśli saldo jest niewystarczające.
Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki
"""
from dataclasses import dataclass

class BrakSrodkowError(Exception):
    pass

@dataclass
class KontoBankowe:
    _saldo: float = 0.0

    @property
    def saldo(self) -> float:
        return self._saldo

    def wplac(self, kwota: float) -> None:
        if kwota < 0:
            raise ValueError("Number cant be negative")
        self._saldo += kwota

    def wyplac(self, kwota: float) -> None:
        if kwota < 0:
            raise ValueError("Number cant be negative")
        if kwota > self._saldo:
            raise BrakSrodkowError("Account balance to low")
        self._saldo -= kwota

    def __str__(self):
        return f"KontoBankowe(saldo={self._saldo:.2f})"


# ===== TEST =====
konto = KontoBankowe(100)

print("Balance:", konto.saldo)

try:
    konto.wplac(50)
    print(f"Balance after deposit: {konto.saldo} ")
except ValueError as e:
    print(f"Error: {e}")

try:
    konto.wplac(-20)
except ValueError as e:
    print(f"Error: {e}")

try:
    konto.wyplac(30)
    print(f"Balance after withdraw: {konto.saldo}")
except (ValueError, BrakSrodkowError) as e:
    print(f"Error: {e}")

try:
    konto.wyplac(-10)
except ValueError as e:
    print(f"Error: {e}")

try:
    konto.wyplac(500)
except BrakSrodkowError as e:
    print(f"Error: {e}")


