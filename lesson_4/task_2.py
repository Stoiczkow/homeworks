'''
 Identyfikator obiektu: Utwórz trzy zmienne ( a , b , c ) z tą samą wartością 256 . Sprawdź
i wyświetl ich id() . Następnie utwórz trzy zmienne z wartością 257 i również sprawdź ich
id() . Czy widzisz różnicę w zachowaniu Pythona? Wyjaśnij dlaczego w komentarzu.
'''

# Zmienna z wartością 256
a = 256
b = 256
c = 256

print(id(a), id(b), id(c))

# Zmienna z wartością 257
x = 257
y = 257
z = 257

print(id(x), id(y), id(z))

# Python "internuje" (przechowuje w pamięci podręcznej) małe liczby całkowite
# od -5 do 256. Oznacza to, że wszystkie zmienne o wartości 256 wskazują
# na ten sam obiekt w pamięci.
# Liczby większe (np. 257) nie są internowane, więc każda zmienna
# ma inny identyfikator (tworzony jest nowy obiekt).
