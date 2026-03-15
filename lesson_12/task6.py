#Zadanie 6 – Własny wyjątek InvalidPasswordError
# Stwórz własny wyjątek InvalidPasswordError. Następnie napisz funkcję ustaw_haslo(haslo), która sprawdza, czy hasło ma co najmniej 8 znaków. Jeśli nie, funkcja powinna podnieść (raise) wyjątek InvalidPasswordError z odpowiednim komunikatem. Napisz kod, który testuje tę funkcję w bloku try...except.
  

#Clalls Exception - taka jest skłądnia

# nowa stwrozna klasa jest jak exception
class InvalidPasswordError(Exception):
    pass    # pas nic nie robi to jest skąłdnia

def ustaw_haslo(password: str):
    # min 8 znaków
    if len(password) <8:
        raise InvalidPasswordError ("Hasło jest za krótki, minimum 8 znaków")           # wyrzucenie wyjątku składnia
    
    return True      # jeżeli prawidłowe True

# przetestowanie w bloku try exception
try:
    print(ustaw_haslo("admin1234"))       # wyowłanie funkcji z dł hasłem (true odp)
    print(ustaw_haslo("admin1"))          # wyowłanie z krótkim hasłem 

except InvalidPasswordError as error:    # przypisujemy błąd do zmiennej 
    print(f"Wystąpił błąd - {error}")
    