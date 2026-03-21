# Zadanie 9 – Walidacja danych w init
# Stwórz klasę RejestracjaUzytkownika. W konstruktorze init przyjmuj email i haslo.
# Wewnątrz konstruktora dodaj walidację:
# Sprawdź, czy email zawiera znak @ . Jeśli nie, podnieś wyjątek ValueError z
# odpowiednim komunikatem.
# Sprawdź, czy haslo ma co najmniej 8 znaków. Jeśli nie, podnieś ValueError. Użyj bloku try...except, aby przetestować tworzenie obiektów z poprawnymi i niepoprawnymi danymi. (challenge)

class RejestracjaUzytkownika:
    def __init__(self, email, haslo):       
        if "@" not in email:
            raise ValueError("Email nie zawiera @")
        if len(haslo) < 8:
            raise ValueError("Hasło musi mieć co najmniej 8 znaków")
        self.haslo = haslo
        self.email = email

# email = input("Podaj email: ")
# haslo = input("Podaj haslo: ")

# try:
#     user = RejestracjaUzytkownika(email, haslo)
#     print("Użytkownik utworzony")
# except ValueError as e:
#     print(f"Błąd: {e}")

try:
    user_1 = RejestracjaUzytkownika("zlyemail", "12345678")
    print("Użytkownik utworzony")
except ValueError as e:
    print(f"User 1: {e}")         

try:
    user_2 = RejestracjaUzytkownika("zly@email", "1234567")
    print("Użytkownik utworzony")
except ValueError as e:
    print(f"User 2: {e}")   

try:
    user_3 = RejestracjaUzytkownika("zly@email", "12345678")
    print("Użytkownik utworzony")
except ValueError as e:
    print(f"User 3: {e}")