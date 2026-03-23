# Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo), która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który testuje tę funkcję w bloku try...except.

class InvalidPasswordError(Exception):
    pass
def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Hasło jest za krótkie.")
    
try:
    ustaw_haslo("1234")
except InvalidPasswordError as e:
    print(f"Błąd: {e}")
        