'''
Łączenie map i filter: Mając listę liczb [-5, 2, 8, -1, 0, 10] , użyj filter do
wybrania tylko liczb dodatnich, a następnie map do obliczenia ich kwadratów. Zrób to w
jednej linijce.
'''

wynik = list(map(lambda x: x*x, filter(lambda x: x > 0, [-5, 2, 8, -1, 0, 10])))

print(wynik)
