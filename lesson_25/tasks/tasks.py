from celery import shared_task
import time


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
    # Tutaj logika wysyłania maili
    print("Podsumowanie wysłane.")


@shared_task
def cleanup_old_logs():
    print("Rozpoczynam czyszczenie starych logów...")
    # Tutaj logika usuwania starych wpisów z bazy danych
    print("Logi wyczyszczone.")


@shared_task
def multiplay(a, b):
    print(a*b)
    return a*b