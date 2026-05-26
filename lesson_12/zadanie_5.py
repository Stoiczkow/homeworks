try:
    with open("nieistniejacy.txt", "r") as plik:
        zawartosc = plik.read()
        print(zawartosc)
except FileNotFoundError:
    print("Blad: Plik 'nieistniejacy.txt' nie zostal znaleziony.")
