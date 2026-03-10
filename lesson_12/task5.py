# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikowi

try:
    with open("nieistniejacy.txt") as file:
        print("Plik otworzony")
except FileNotFoundError:
    print("Nie znaleziono pliku")