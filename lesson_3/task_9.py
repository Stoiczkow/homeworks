'''
Bramki logiczne: Napisz program, który poprosi o dwie wartości logiczne ( True lub
False ). Niech użytkownik wprowadza 1 dla True i 0 dla False . Program powinien
wyświetlić wyniki operacji AND oraz OR dla tych dwóch wartości.
'''

a = int(input("Podaj pierwszą wartość (1 = True, 0 = False): "))
b = int(input("Podaj drugą wartość (1 = True, 0 = False): "))

# Zamiana 1/0 na wartości logiczne
x = bool(a)
y = bool(b)

wynik_and = x and y
wynik_or = x or y

print(f"Wynik AND: {wynik_and}")
print(f"Wynik OR: {wynik_or}")
