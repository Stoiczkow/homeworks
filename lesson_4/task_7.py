'''
Błąd konwersji: Napisz program, który świadomie spróbuje przekonwertować słowo
"Python" na liczbę całkowitą. Uruchom go, zobacz błąd ValueError , a następnie
"napraw" program, umieszczając błędną linię w komentarzu i dodając wyjaśnienie, dlaczego
kod nie działał
'''

# liczba = int("Python")  

# Powyższa linia powoduje błąd:
# ValueError: invalid literal for int() with base 10: 'Python'

# Funkcja int() może konwertować tylko napisy, które wyglądają jak liczby
# (np. "10", "3", "-5"). Słowo "Python" nie jest liczbą, więc konwersja jest niemożliwa.

print("Program działa — błędna linia została zakomentowana.")
