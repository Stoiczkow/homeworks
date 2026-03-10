class InvalidPasswordError(Exception):
    pass


def ustaw_haslo(password: str):
    if len(password) < 8:
        raise InvalidPasswordError("Hasło jest za krótkie. Minimum 8 znaków")
    
    return True


try:
    print(ustaw_haslo("admin1234"))
    print(ustaw_haslo("123"))
except InvalidPasswordError as error:
    print(f"Wystąpił błąd - {error}")