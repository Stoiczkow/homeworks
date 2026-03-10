# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo),
# która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść
# (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który
# testuje tę funkcję w bloku try...except

class InvalidPasswordError(Exception):
    pass

def ustaw_haslo(haslo):
    if len(haslo) < 8:
        raise InvalidPasswordError("Password too short")
    

try:
    ustaw_haslo("abc")
except InvalidPasswordError as e:
    print(f"Błąd: {e}")

try:
    ustaw_haslo("abcabcabcabc")
except InvalidPasswordError as e:
    print(f"Błąd: {e}")