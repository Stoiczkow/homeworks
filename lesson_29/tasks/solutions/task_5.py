'''
Stwórz zadanie count_users(), które liczy wszystkich użytkowników w bazie danych
(User.objects.count()) i drukuje wynik w konsoli workera
'''

from celery import shared_task
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def count_users():
    total = User.objects.count()
    print(f"Liczba użytkowników: {total}")
    return