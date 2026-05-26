class MetaWalidujMetody(type):
    def __new__(mcs, nazwa, bazy, przestrzen):
        for nazwa_metody, obj in przestrzen.items():
            if callable(obj) and not nazwa_metody.startswith("__"):
                if not obj.__doc__:
                    raise TypeError(
                        f"Metoda '{nazwa_metody}' w klasie '{nazwa}' nie ma docstringa."
                    )
        return super().__new__(mcs, nazwa, bazy, przestrzen)


class PoprawnaKlasa(metaclass=MetaWalidujMetody):
    def metoda_a(self):
        """Metoda A wykonuje jakies dzialanie."""
        pass

    def metoda_b(self):
        """Metoda B wykonuje inne dzialanie."""
        pass


print("PoprawnaKlasa utworzona pomyslnie.")

try:
    class NiepoprawnaKlasa(metaclass=MetaWalidujMetody):
        def metoda_z_docstringiem(self):
            """Ta metoda ma docstring."""
            pass

        def metoda_bez_docstringa(self):
            pass

except TypeError as e:
    print(f"TypeError: {e}")
