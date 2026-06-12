'''
2. Kalkulator BMI: Napisz program, który zapyta użytkownika o jego wagę w kilogramach i
wzrost w metrach. Oblicz i wyświetl wskaźnik masy ciała (BMI) według wzoru: BMI = waga
/ (wzrost * wzrost)
'''

waga = float(input("Podaj swoją wagę w kilogramach: "))
wzrost = float(input("Podaj swój wzrost w metrach: "))

bmi = waga / (wzrost * wzrost)

print(f"Twoje BMI wynosi: {bmi}")
