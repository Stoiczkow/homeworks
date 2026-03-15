# Zadanie 9 – Klasa KontoBankowe z property i wyjątkami

# #Stwórz klasę KontoBankowe za pomocą @dataclass, która ma atrybut _saldo (prywatne).
# Stwórz właściwość ( @property ) saldo , która tylko odczytuje wartość _saldo .
# Stwórz metodę wplac(kwota) , która dodaje kwotę do salda. Metoda powinna podnosić
# ValueError , jeśli kwota jest ujemna.
# Stwórz metodę wyplac(kwota) , która odejmuje kwotę od salda. Metoda powinna
# podnosić ValueError , jeśli kwota do wypłaty jest ujemna, oraz własny wyjątek
# BrakSrodkowError , jeśli saldo jest niewystarczające.
# Przetestuj działanie klasy, obsługując wszystkie możliwe wyjątki.


# import biblioteki dataclass - autmatycznie tworzy __init__
from dataclasses import dataclass

# Własny wyjątek dla konto jest niewstarczająće
class lacofmoney(Exception):
    pass

# Definicja klasy - tworzymy klasę
@dataclass
class Bankacoount:
    _saldo: float   # atrybut klasy

# propery pozwala odczytać saldo jako zmienną możemy wtedy pisać self.saldo bez ()
    @property
    def saldo(self):
        return self._saldo
    
    # wpłacanie gotówki
    def add(self, suma):
        if suma < 0:
            raise ValueError("Kwota nie może być ujemna: ") # bład
        self._saldo += suma

    # Wypłacanie gotówki
    def subtract(self, suma):
        if suma < 0:
            raise ValueError("Kwota wpłaty nie może być ujemna")    # bład
        if suma > self._saldo:
            raise lacofmoney("Brak wystarczającyh środków na koncie")   # błąd
        self._saldo -= suma

# test działa klasy

#Tworzymy obiekt
account = Bankacoount(200)

# Obsłyga wyjątków
try:
    # wpłacanie
    account.add(50)
    print(f"Saldo po wplacie {account.saldo}")

    # wypłacanie
    account.subtract(100)
    print(f"Saldo po wyplacie {account.saldo}")

    # Wypłacanie error
    account.subtract(1000) # wywołanie lackofmoney

# obsługa błędów
except ValueError as e:
    print("Bląd wartosici", e)

except lacofmoney as e:
    print("Błąd", e)

print(f"Aktualna kwota na koncie: {account.saldo}")
