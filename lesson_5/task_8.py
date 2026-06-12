'''
Wyszukiwarka w liście: Stwórz listę imion: imiona = ["Anna", "Jan", "Piotr",
"Kasia"] . Poproś użytkownika o podanie imienia do wyszukania. Użyj pętli for z
instrukcją break oraz blokiem else , aby:
- Jeśli imię zostanie znalezione, wyświetlić "Znaleziono!" i przerwać pętlę.
- Jeśli pętla zakończy się bez znalezienia imienia, wyświetlić "Nie znaleziono imienia na
liście."
'''

imiona = ["Anna", "Jan", "Piotr", "Kasia"]
szukane = input("Podaj imię do wyszukania: ")

for imie in imiona:
    if imie == szukane:
        print("Znaleziono!")
        break
else:
    print("Nie znaleziono imienia na liście.")

