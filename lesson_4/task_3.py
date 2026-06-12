'''
Porównanie is vs == : Utwórz dwie różne listy lista1 = [1, 1] i lista2 = [1, 1] .
Sprawdź wynik porównania lista1 is lista2 oraz lista1 == lista2 . Wyświetl wyniki
i w komentarzu wyjaśnij, dlaczego są różne.
'''

lista1 = [1, 1]
lista2 = [1, 1]

print("lista1 is lista2:", lista1 is lista2)
print("lista1 == lista2:", lista1 == lista2)

# '==' porównuje wartości – listy mają takie same elementy, więc wynik to True.
# 'is' porównuje tożsamość obiektów – czy to ten sam obiekt w pamięci.
# lista1 i lista2 to dwie różne listy, więc wynik to False.
