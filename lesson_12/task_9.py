# 9. 🧠 Zadanie 9 – Klasa KontoBankowe z property i wyjątkami
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

@dataclass
class KontoBankowe:
    _saldo: float

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):        
        if kwota < 0:
            raise ValueError("Błąd! Ujemna kwota do wpłaty!")
        self._saldo += kwota
        
    def wyplac(self, kwota):        
        if kwota < 0:
            raise ValueError("Błąd! Ujemna kwota do wypłaty")
        elif kwota > self.saldo:
            raise BrakSrodkowError("Błąd! Niewystarczające saldo!")
        self._saldo -= kwota
        
def main():
    try:
        new_konto = KontoBankowe(1000)
        print(new_konto.saldo)
        new_konto.wplac(500)
        print(new_konto.saldo)
        new_konto.wyplac(800)
        print(new_konto.saldo)
        #new_konto.wyplac(-100)
        #new_konto.wyplac(3000)
        #new_konto.wplac(-200)

    except (ValueError, BrakSrodkowError) as e:
        print(e)
main()