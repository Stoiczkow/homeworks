'''
Konwersja na wielkie litery: Użyj funkcji map() , aby przekształcić listę imion 
imiona = ["anna", "piotr", "kasia"] w listę imion pisanych wielką literą
'''

imiona = ["anna", "piotr", "kasia"]

imiona_duze = list(map(str.capitalize, imiona))

print(imiona_duze)

