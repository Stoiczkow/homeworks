# 5. ✏ Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikowi.

try:
    file = open("file.txt")
    print(file.read())
except FileNotFoundError:
    print("Nie można znaleźć takiego pliku!")