'''
Stwórz w pliku tasks.py proste zadanie o nazwie hello_world, które po prostu drukuje w
konsoli workera napis "Hello from Celery!". Stwórz widok Django, który po wejściu na
odpowiedni URL wywoła to zadanie
'''

from celery import shared_task

@shared_task
def hello_world():
    print('Hello from Celery')