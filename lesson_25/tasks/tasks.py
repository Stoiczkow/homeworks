from celery import shared_task
import time
from django.contrib.auth.models import User
from django.utils import timezone

@shared_task
def hello_world():
    print("Hello from Celery!")

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
    time.sleep(10)  # Symulacja opóźnienia związanego z serwerem SMTP
    print(f"Mail do {user_email} wysłany.")
    return True

@shared_task
def send_periodic_summary(user_emails):
    print(f"Wysyłanie podsumowania do {len(user_emails)} użytkowników...")
    # Tutaj logika wysyłania maili
    print("Podsumowanie wysłane.")


@shared_task
def cleanup_old_logs():
    print("Rozpoczynam czyszczenie starych logów...")
    # Tutaj logika usuwania starych wpisów z bazy danych
    print("Logi wyczyszczone.")

@shared_task
def multiply(a, b):
    result = a * b
    print(f"Rozpoczynam mnożenie {a} przez {b}...")
    
    return result

@shared_task
def log_timestamp():

    current_time = datetime.now()

    with open("log.txt", "a") as file:
        file.write(f"{current_time} log_timestamp\n")

    print(f"Zapisano: {current_time}")

@shared_task
def count_users():

    users_count = User.objects.count()

    print(f"Obecna liczba użytkowników: {users_count}")
    return users_count

@shared_task
def  update_user_last_login(user_id):
    try:
        user = User.objects.get(id=user_id)
        # user.last_login = datetime.now()
        user.last_login = timezone.now()
        user.save()
        print(f"Zaktualizowano last_login dla użytkownika {user.username}")
    except User.DoesNotExist:
        print(f"Użytkownik o id {user_id} nie istnieje.")


@shared_task
def video_task():
    print("Przetwarzanie wideo rozpoczęte!")
    time.sleep(15)  
    print("Przetwarzanie wideo zakończone!")

    