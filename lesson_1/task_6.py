'''
Konwerter systemów liczbowych:
Utwórz plik task6_converter.py .
Poproś użytkownika o liczbę całkowitą i wyświetl ją w formacie dwójkowym i
szesnastkowym
'''

liczba = int(input("Podaj liczbę całkowitą: "))

binarnie = bin(liczba)
szesnastkowo = hex(liczba)

print(f"Liczba {liczba} w systemie dwójkowym: {binarnie}")
print(f"Liczba {liczba} w systemie szesnastkowym: {szesnastkowo}")
