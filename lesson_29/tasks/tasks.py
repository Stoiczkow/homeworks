from celery import shared_task
import time, datetime
from django.utils import timezone
from django.contrib.auth.models import User
from .models import EmailNotification, LogEntry
from datetime import timedelta

@shared_task
def add(x, y):
    """Proste zadanie, które dodaje dwie liczby."""
    return x + y

@shared_task
def simulate_cpu_bound_task(duration):
    """
    Symuluje długotrwałe zadanie CPU-bound, np. generowanie raportu.
    Używamy time.sleep(), aby zasymulować opóźnienie.
    """
    print(f"Rozpoczynam zadanie, które potrwa {duration} sekund...")

    time.sleep(duration)
    print("Zadanie zakończone.")
    return f"Raport wygenerowany pomyślnie po {duration} sekundach."

@shared_task
def send_welcome_email(user_email):
    """
    Symuluje wysyłanie maila powitalnego.
    W rzeczywistej aplikacji tutaj znalazłby się kod do wysyłki maila.
    """
    print(f"Wysyłanie maila powitalnego do {user_email}...")
    time.sleep(10) # Symulacja opóźnienia związanego z serwerem SMTP
    print(f"Mail do {user_email} wysłany.")
    return True

@shared_task
def send_periodic_summary(user_emails):
    print(f"Wysyłanie podsumowania do {len(user_emails)} użytkowników...")
    print("Podsumowanie wysłane.")

@shared_task
def cleanup_old_logs():
    print("Rozpoczynam czyszczenie starych logów...")
    print("Logi wyczyszczone.")

#task1
@shared_task
def hello_world():
    print("Hello from Celery!")

#task2
@shared_task
def multiply(a: float, b: float)->float:
    print(a * b)
    return a * b

#task3
@shared_task
def log_timestamp():
    now_time = datetime.datetime.now()
  
    print(f"Aktualny czas {str(now_time)}")
    return now_time

#task5
@shared_task
def count_user():
    all_users = User.objects.count()
    print(f"liczba uzytkownikow wynosi {all_users}")
    return all_users    

#task7
@shared_task
def update_user_last_login(user_id):
    user = User.objects.all().get(id=user_id)
    user.last_login = timezone.now()
    user.save()
    print(f"Znaleziono uzytkownika o id {user_id}")
    return user

#task 8
@shared_task
def video_processing_simulation():
    print(f"Symulacja procesu video rozpoczeta")
    time.sleep(15)
    print(f"Symulacja procesu video zakonczona")
    return True



#task 10
@shared_task
def task_EmailNotification(id_email):

    try:
        object_id = EmailNotification.objects.get(id=id_email)
        time.sleep(14)
        object_id.sent_at = timezone.now()
        object_id.save()
    except EmailNotification.DoesNotExist:
        print("Obiekt nie istnieje")

#task12
@shared_task
def clear_log_Entry():

    time_difference = timezone.now() - timezone.timedelta(days=90)
    deleted_info = LogEntry.objects.filter(create_at__lt=time_difference).delete()


    return f"Usunięto logi starsze niż 90 dni."

