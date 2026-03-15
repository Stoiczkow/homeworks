# Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat użytkownikowi.

try:
    file = open("data.txt")
    # dodanie jeżeli plik się wczyta odczytu
    print(file.read())
    
    # obsługa wyjątku
except FileNotFoundError:
    print("Plik nie istnieje")