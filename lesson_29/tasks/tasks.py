from celery import shared_task
import time
from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup

from django.contrib.auth import get_user_model
from django.utils import timezone
from .models import EmailNotification, LogEntry, Website


User = get_user_model()

@shared_task
def add(x, y):
    """Proste zadanie, które dodaje dwie liczby."""
    return x + y

# Zadanie 2 – Zadanie z argumentami
# Zadania-wyzwania (challenge)
# Napisz zadanie multiply(a, b), które przyjmuje dwie liczby i zwraca ich iloczyn. W widoku
# stwórz prosty formularz HTML z dwoma polami, z których pobierzesz liczby i przekażesz je
# do zadania Celery.
@shared_task
def multiply(x, y):
    """Proste zadanie, które mnoży dwie liczby."""
    return x* y


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

# Zadanie 1 – Pierwsze zadanie
# Stwórz w pliku tasks.py proste zadanie o nazwie hello_world, które po prostu drukuje w
# konsoli workera napis "Hello from Celery!". Stwórz widok Django, który po wejściu na
# odpowiedni URL wywoła to zadanie.   
@shared_task
def hello_world():
    print("Hello from cellery..")

# Zadanie 3 – Zapis do pliku
# Stwórz zadanie log_timestamp(), które zapisuje aktualną datę i godzinę do pliku log.txt    
@shared_task
def log_timestamp():
    print("Zapisuje date do pliku..")
    
    with open("log.txt", "w") as f:
        f.write(str(datetime.now()))
        
# Zadanie 5 – Zmiana w bazie danych
# Stwórz zadanie count_users(), które liczy wszystkich użytkowników w bazie danych
# (User.objects.count()) i drukuje wynik w konsoli workera.       
@shared_task
def count_users():
    count = User.objects.count()
    print(f"Liczba użytkowników: {count}")
    return count

# Zadanie 7 – Przekazywanie ID obiektu
# Stwórz zadanie update_user_last_login(user_id), które przyjmuje ID użytkownika, znajduje
# go w bazie i aktualizuje jego pole last_login na aktualny czas
@shared_task
def update_user_last_login(user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return None
    
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])
    
    return user

# Zadanie 8 – Prosta symulacja
# Napisz zadanie, które symuluje przetwarzanie wideo przez 15 sekund (time.sleep(15)).
# Widok, który je wywołuje, powinien natychmiast zwrócić komunikat "Przetwarzanie wideo
# rozpoczęte!"
@shared_task
def simulate_processing_video():
    print("Przetwarzanie wideo rozpoczęte...")
    time.sleep()
    print("Przetwarzanie wideo zakończone...")

# 🧠 Zadanie 10 – Powiadomienie mailowe
# Rozbuduj zadanie z symulacją wysyłki maila. Stwórz prosty model EmailNotification z
# polami recipient_email, subject, body i sent_at (nullable). Zadanie Celery powinno przyjąć
# ID obiektu tego modelu, wysłać "maila" (czyli zasymulować opóźnienie) i po zakończeniu
# zaktualizować pole sent_at na aktualny czas

@shared_task
def send_email(notification_id):
    
    try:
        email_notification = EmailNotification.objects.get(
            id=notification_id
            )
    except EmailNotification.DoesNotExist:
        return None
    
    print(
        f"Wysyłanie maila do "
        f"{email_notification.recipient_email}..."
    )
    
    time.sleep(15)
    
    print("Mail wysłany.")
    
    email_notification.sent_at = timezone.now()
    email_notification.save(update_fields=["sent_at"])
    
    return email_notification.id

# Zadanie 11 – Śledzenie postępu zadania
# Stwórz zadanie, które w pętli od 1 do 100 wykonuje jakąś operację, śpiąc 0.1 sekundy w
# każdej iteracji. Po każdej iteracji zadanie powinno aktualizować swój stan, informując o
# postępie. Stwórz drugi endpoint w Django (/task-status/<task_id>/), który będzie zwracał
# aktualny postęp zadania

@shared_task(bind=True)
def do_operation(self):
    
    total = 100
    
    for i in range(1, total + 1):
        time.sleep(20)
        
        self.update_state(
            state="PROGRESS", 
            meta={
                'current': i,
                'total': 100
                }
            )
        
    return {
        "current": total,
        "total": total,
        "status": "completed"
    }
    
# Zadanie 12 – Czyszczenie bazy danych
# Napisz zadanie, które usuwa z bazy wszystkie obiekty modelu LogEntry (musisz go
# najpierw stworzyć) starsze niż 90 dni. Uruchom to zadanie za pomocą Celery Beat raz
# dziennie.

@shared_task(bind=True)
def clear_logs():
    to_delete = timezone.now() - timedelta(days=90)
    logs_to_delete = LogEntry.objects.filter(created_at__lt=to_delete)
    
    logs_to_delete.delete()   
            
    return f'Usunięto logi starsze niż 90 dni'
    
# Zadanie 13 – Web scraping w tle
# Stwórz zadanie, które używa biblioteki requests i BeautifulSoup4 do pobrania tytułu strony
# https://example.com i zapisania go w bazie danych. Zadanie to ma być uruchamiane co
# godzinę.

@shared_task
def get_website_title():  
    try:
        response = requests.get("https://example.com")
        
        soup = BeautifulSoup(response.text, "html.parser")

        Website.objects.create(title=soup.title.text)
        
        return f'Utworzono obiekt strony z tytulem {soup.title.text}'
        
    except requests.RequestException as e:
        print(f"Błąd pobierania strony: {e}")