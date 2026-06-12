'''
Praca z f-stringami: Poproś użytkownika o jego imię i rok urodzenia. Oblicz jego
przybliżony wiek i wyświetl komunikat w formacie: "Cześć, [Imię]! W 2025 roku
będziesz mieć około [Wiek] lat."
'''

imie = input("Jak masz na imię? ")
rok_urodzenia = int(input("Podaj rok urodzenia: "))

wiek_w_2025 = 2025 - rok_urodzenia

print(f"Cześć, {imie}! W 2025 roku będziesz mieć około {wiek_w_2025} lat.")
