'''
Tylko samogłoski: Poproś użytkownika o zdanie. Użyj pętli for oraz instrukcji continue ,
aby wyświetlić tylko samogłoski z tego zdania. (Wskazówka: if litera not in
"aeiouy": continue ).
'''

zdanie = input("Podaj zdanie: ")

for litera in zdanie.lower():
    if litera not in "aeiouy":
        continue
    print(litera)
