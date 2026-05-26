class KalkulatorWalut:
    @staticmethod
    def usd_na_pln(kwota_usd):
        kurs = 4.0
        return kwota_usd * kurs


wynik = KalkulatorWalut.usd_na_pln(100)
print(f"100 USD = {wynik} PLN")
