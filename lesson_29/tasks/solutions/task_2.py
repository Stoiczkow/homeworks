'''
Napisz zadanie multiply(a, b), które przyjmuje dwie liczby i zwraca ich iloczyn. W widoku
stwórz prosty formularz HTML z dwoma polami, z których pobierzesz liczby i przekażesz je
do zadania Celery
'''

from celery import shared_task

@shared_task
def multiply(a, b):
    result = a * b
    print(f"Mnożenie - {a} x {b}) = {result}")
    return result