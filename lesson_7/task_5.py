'''
Iloczyn elementów: Użyj funkcji reduce() , aby obliczyć iloczyn (wynik mnożenia)
wszystkich liczb w liście [1, 2, 3, 4, 5] .
'''

from functools import reduce

lista = [1, 2, 3, 4, 5]

iloczyn = reduce(lambda a, b: a * b, lista)

print(iloczyn)
