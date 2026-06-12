'''
iterowanie słowa: Poproś użytkownika o podanie słowa. Użyj pętli for , aby wyświetlić
każdą literę tego słowa w osobnej linii, poprzedzoną jej indeksem. Przykład dla "Kot": 0:
K , 1: o , 2: t
'''

slowo = input("Podaj słowo: ")

for indeks, litera in enumerate(slowo):
    print(f"{indeks}: {litera}")
