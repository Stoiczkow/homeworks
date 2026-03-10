# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.

from dataclasses import dataclass

class InsufficientFundsError(Exception):
    pass

@dataclass
class BankAccount:
    _balance: float = 0.0

    @property
    def balance(self):
        return self._balance
    
    def wplac(self, amount):
        if amount < 0:
            raise ValueError("Kwota do wpłaty nie może być ujemna.")
        self._balance += amount
    
    def wyplac(self, amount):
        if amount < 0:
            raise ValueError("Kwota do wypłaty nie może być ujemna.")
        if amount > self._balance:
            raise InsufficientFundsError("Niewystarczające środki na koncie.")
        self._balance -= amount

account = BankAccount()
try:
    account.wplac(100)
    print(f"Saldo po wpłacie: {account.balance}")
    account.wyplac(30)
    print(f"Saldo po wypłacie: {account.balance}")
    account.wyplac(80)  # To powinno wywołać InsufficientFundsError
except ValueError as ve:
    print(f"Wystąpił błąd: {ve}")
except InsufficientFundsError as ife:
    print(f"Wystąpił błąd: {ife}")

