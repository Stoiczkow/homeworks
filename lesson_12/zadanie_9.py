from dataclasses import dataclass, field


class BrakSrodkowError(Exception):
    pass


@dataclass
class KontoBankowe:
    _saldo: float = field(default=0.0)

    @property
    def saldo(self):
        return self._saldo

    def wplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wplaty nie moze byc ujemna.")
        self._saldo += kwota

    def wyplac(self, kwota):
        if kwota < 0:
            raise ValueError("Kwota wyplaty nie moze byc ujemna.")
        if kwota > self._saldo:
            raise BrakSrodkowError(f"Brak srodkow. Saldo: {self._saldo}, ządana kwota: {kwota}")
        self._saldo -= kwota


konto = KontoBankowe()

try:
    konto.wplac(1000)
    print(f"Po wplacie: {konto.saldo}")

    konto.wyplac(200)
    print(f"Po wyplacie: {konto.saldo}")

    konto.wplac(-50)
except ValueError as e:
    print(f"ValueError: {e}")

try:
    konto.wyplac(2000)
except BrakSrodkowError as e:
    print(f"BrakSrodkowError: {e}")

try:
    konto.wyplac(-10)
except ValueError as e:
    print(f"ValueError: {e}")
