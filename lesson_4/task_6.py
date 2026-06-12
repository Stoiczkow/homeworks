'''
Prawda czy fałsz?: Napisz program, który prosi użytkownika o wpisanie dowolnego tekstu.
Następnie, używając konwersji na bool , sprawdź, czy wpisany tekst jest "prawdziwy"
(niepusty) i wyświetl odpowiedni komunikat.
'''

tekst = input("Wpisz dowolny tekst: ")

if bool(tekst):
    print("Wpisałeś tekst – wartość jest prawdziwa (True).")
else:
    print("Nic nie wpisałeś – wartość jest fałszywa (False).")
