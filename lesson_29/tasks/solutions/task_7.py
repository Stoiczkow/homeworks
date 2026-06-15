'''
Stwórz zadanie update_user_last_login(user_id), które przyjmuje ID użytkownika, znajduje
go w bazie i aktualizuje jego pole last_login na aktualny czas.
'''


from celery import shared_task
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()

@shared_task
def update_user_last_login(user_id):
    try:
        user = User.objects.get(id=user_id)
        user.last_login = timezone.now()
        user.save(update_fields=["last_login"])
        print(f"Zaktualizowano last_login dla użytkownika ID={user_id}")
        return True
    except User.DoesNotExist:
        print(f"Użytkownik o ID={user_id} nie istnieje")
        return False
