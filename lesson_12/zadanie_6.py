class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Haslo musi miec co najmniej 8 znakow.")
    print(f"Haslo '{haslo}' zostalo ustawione pomyslnie.")


try:
    ustaw_haslo("abc")
except InvalidPasswordError as e:
    print(f"Blad: {e}")

try:
    ustaw_haslo("bezpiecznehaslo")
except InvalidPasswordError as e:
    print(f"Blad: {e}")
