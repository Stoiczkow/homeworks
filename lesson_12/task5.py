try:
    file = open("config.json")
    print(file.read())
except FileNotFoundError:
    print('Plik o podanej nazwie nie istnieje')