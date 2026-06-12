'''
Średnia ocen: Napisz funkcję oblicz_srednia(*args) , która przyjmuje dowolną liczbę
ocen (argumentów pozycyjnych) i zwraca ich średnią arytmetyczną. Jeśli nie podano żadnej
oceny, powinna zwrócić 0
'''

def oblicz_srednia(*args):
    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(oblicz_srednia(5, 4, 3))
print(oblicz_srednia())  # zwróci 0
