"""
Dziennik użytkownika:
Program w pętli prosi użytkownika o wpisanie jednej linii tekstu.
Każda linia jest dopisywana do pliku dziennik.txt (tryb 'a').
Program kończy działanie, gdy użytkownik wpisze "koniec".
"""

while True:
    tekst = input("Wpisz tekst (lub 'koniec' aby zakończyć): ")

    if tekst.lower() == "koniec":
        break

    with open("dziennik.txt", "a", encoding="utf-8") as f:
        f.write(tekst + "\n")
