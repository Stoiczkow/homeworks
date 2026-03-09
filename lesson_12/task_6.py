# Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except.

class InvalidPasswordError(Exception):
    pass

def ustaw_haslo(password: str):
    if len(password) < 8:
        raise InvalidPasswordError("Haslo za krotkie, musi mieć dlugosc min 8 ")
        return True
    
try:
    print(ustaw_haslo("dlugie_haslo"))
    print(ustaw_haslo("krotkie"))
except InvalidPasswordError as e:
    print(f"Błąd: {e}")
