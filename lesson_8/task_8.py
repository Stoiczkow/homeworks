"""
Walidacja hasła v2:
Funkcja powinna zwracać listę błędów walidacji.
Jeśli lista błędów nie jest pusta, rzuć wyjątek BladWalidacjiError,
przekazując do niego tę listę.
"""

class BladWalidacjiError(Exception):
    def __init__(self, bledy):
        super().__init__("Błędy walidacji hasła.")
        self.bledy = bledy


def waliduj_haslo(haslo: str):
    bledy = []

    if len(haslo) < 8:
        bledy.append("Hasło musi mieć co najmniej 8 znaków.")
    if not any(z.isupper() for z in haslo):
        bledy.append("Hasło musi zawierać wielką literę.")
    if not any(z.isdigit() for z in haslo):
        bledy.append("Hasło musi zawierać cyfrę.")

    if bledy:
        raise BladWalidacjiError(bledy)

    return True



waliduj_haslo("abc")
