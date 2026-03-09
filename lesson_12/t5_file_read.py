# Zadanie 5 – Odczyt pliku
# Napisz program, który próbuje otworzyć i odczytać plik o nazwie nieistniejacy.txt. Użyj bloku
# try...except, aby obsłużyć wyjątek FileNotFoundError i wyświetlić przyjazny komunikat
# użytkownikow

def file_reader():

    try:
        with open("nieistniejacy.txt", mode="r", encoding="utf-8") as f:
            print(f.readline())
    except FileNotFoundError:
        print("Podany plik nie isnieje")

file_reader()