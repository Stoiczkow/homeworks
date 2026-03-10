# Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki

from dataclasses import dataclass

@dataclass
class KontoBankowe:
    _saldo: float = 0

    class BrakSrodkowError(Exception):
        pass

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError
        else:
            self._saldo =+ kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError
        elif self._saldo - kwota < 0:
            raise self.BrakSrodkowError
        else:
            self._saldo =- kwota

# Przykłady użycia

account = KontoBankowe(1000)

print(f"Saldo początkowe: {account.saldo}")

account.wplac(5000)
print(f"Saldo po wpłacie 5000: {account.saldo}")

try:
    account.wplac(-100)
except ValueError:
    print("Wystąpił błąd przy próbie dodania minusowego salda")

try:
    account.wyplac(-500)
except ValueError:
    print("Wystąpił błąd przy próbie odjęcia minusowego salda")

account.wyplac(600)
print(f"Saldo po wypłacie 600: {account.saldo}")

print("Tu wystąpi customowy błąd po próbie wypłacenia większej ilości środków niż dostępne na koncie:")
account.wyplac(500000)