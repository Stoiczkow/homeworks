'''
Identyfikator po zmianie: Utwórz zmienną x = 10 . Wyświetl jej id() . Następnie
przypisz do x nową wartość x = x + 1 . Ponownie wyświetl id() . Czy identyfikator się
zmienił? Dlaczego? Odpowiedz w komentarzu.
'''

x = 10
print("ID przed zmianą:", id(x))

x = x + 1
print("ID po zmianie:", id(x))

# Liczby całkowite są niemutowalne. Operacja x = x + 1 tworzy NOWY obiekt w pamięci.
# Dlatego identyfikator (id) zmienia się po przypisaniu nowej wartości.
