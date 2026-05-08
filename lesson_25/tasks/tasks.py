import csv
import random
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

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
def hello_world():
    print("Hello from Celery!")
    return "Hello from Celery!"


@shared_task
def multiply(a, b):
    return int(a) * int(b)


@shared_task
def log_timestamp():
    path = settings.BASE_DIR / "log.txt"
    with path.open("a") as file:
        file.write(f"{timezone.now().isoformat()}\n")
    return str(path)


@shared_task
def count_users():
    count = User.objects.count()
    print(f"Liczba użytkowników: {count}")
    return count


@shared_task
def update_user_last_login(user_id):
    user = User.objects.get(id=user_id)
    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])
    return user.id


@shared_task
def process_video():
    time.sleep(15)
    return "Przetwarzanie wideo zakończone."


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
def send_email_notification(notification_id):
    from .models import EmailNotification

    notification = EmailNotification.objects.get(id=notification_id)
    time.sleep(3)
    notification.sent_at = timezone.now()
    notification.save(update_fields=["sent_at"])
    return notification.id


@shared_task(bind=True)
def progress_task(self):
    for i in range(1, 101):
        time.sleep(0.1)
        self.update_state(state="PROGRESS", meta={"current": i, "total": 100})
    return {"current": 100, "total": 100}


@shared_task
def cleanup_old_log_entries():
    from .models import LogEntry

    cutoff = timezone.now() - timezone.timedelta(days=90)
    deleted, _ = LogEntry.objects.filter(created_at__lt=cutoff).delete()
    return deleted


@shared_task
def scrape_example_title():
    from .models import ScrapedPage

    response = requests.get("https://example.com", timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.string if soup.title else "No title"
    page = ScrapedPage.objects.create(url="https://example.com", title=title)
    return page.id


@shared_task
def generate_users_csv(report_id):
    from .models import UserReport

    media_dir = settings.BASE_DIR / "media"
    media_dir.mkdir(exist_ok=True)
    file_path = media_dir / f"users-report-{report_id}.csv"

    with file_path.open("w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["username", "email"])
        for user in User.objects.order_by("username"):
            writer.writerow([user.username, user.email])

    report = UserReport.objects.get(id=report_id)
    report.file_path = str(file_path.relative_to(settings.BASE_DIR))
    report.generated_at = timezone.now()
    report.save(update_fields=["file_path", "generated_at"])
    return report.id


@shared_task(bind=True)
def failing_url_task(self):
    try:
        requests.get("https://invalid.localhost.example", timeout=2)
    except requests.RequestException as exc:
        raise self.retry(exc=exc, countdown=60, max_retries=3)


@shared_task
def classify_uploaded_image(image_id):
    from PIL import Image

    from .models import UploadedImage

    uploaded = UploadedImage.objects.get(id=image_id)
    with Image.open(uploaded.image.path) as image:
        mode = "grayscale" if image.mode in ("L", "1") else "color"
        uploaded.classification_result = f"{mode}, {image.width}x{image.height}"
        uploaded.save(update_fields=["classification_result"])
    return uploaded.classification_result


@shared_task
def generate_random_number():
    return random.randint(1, 100)


@shared_task
def multiply_by_ten(value):
    return value * 10


@shared_task
def save_chain_result(value):
    path = settings.BASE_DIR / "chain_result.txt"
    path.write_text(str(value))
    return value


@shared_task
def critical_email_task(email):
    print(f"Krytyczny email do {email}")
    return True
