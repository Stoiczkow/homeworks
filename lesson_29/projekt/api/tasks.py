import csv
import os
import time
from datetime import timedelta

import requests
from bs4 import BeautifulSoup
from celery import chain, shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone

from .models import EmailNotification, LogEntry, ScrapedTitle, UploadedImage


# ── Zadanie 3 – zapis znacznika czasu do pliku ──────────────────────────────
@shared_task
def log_timestamp():
    log_path = settings.BASE_DIR / 'log.txt'
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{timezone.now():%Y-%m-%d %H:%M:%S}\n")


# ── Zadanie 5 – liczenie użytkowników ───────────────────────────────────────
@shared_task
def count_users():
    count = User.objects.count()
    print(f"Liczba użytkowników w bazie: {count}")
    return count


# ── Zadanie 7 – aktualizacja last_login użytkownika ─────────────────────────
@shared_task
def update_user_last_login(user_id):
    try:
        user = User.objects.get(pk=user_id)
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        print(f"Zaktualizowano last_login dla użytkownika {user.username}")
    except User.DoesNotExist:
        print(f"Użytkownik o ID={user_id} nie istnieje")


# ── Zadanie 8 – symulacja przetwarzania wideo ────────────────────────────────
@shared_task
def process_video():
    time.sleep(15)
    print("Przetwarzanie wideo zakończone!")
    return "Wideo przetworzone"


# ── Zadanie 9 – zadanie multiply (używane w enqueue_tasks) ──────────────────
@shared_task
def multiply(a, b):
    return a * b


# ── Zadanie 10 – wysyłka powiadomienia email ─────────────────────────────────
@shared_task(queue='priority_queue')
def send_notification_email(notification_id):
    try:
        notification = EmailNotification.objects.get(pk=notification_id)
        # Symulacja wysyłki (opóźnienie 2 sekundy)
        time.sleep(2)
        notification.sent_at = timezone.now()
        notification.save(update_fields=['sent_at'])
        print(f"Mail wysłany do {notification.recipient_email}: {notification.subject}")
    except EmailNotification.DoesNotExist:
        print(f"EmailNotification o ID={notification_id} nie istnieje")


# ── Zadanie 11 – śledzenie postępu zadania ───────────────────────────────────
@shared_task(bind=True)
def long_task_with_progress(self):
    total = 100
    for i in range(1, total + 1):
        time.sleep(0.1)
        self.update_state(
            state='PROGRESS',
            meta={'current': i, 'total': total, 'percent': int(i / total * 100)}
        )
    return {'current': total, 'total': total, 'percent': 100, 'result': 'Zakończono'}


# ── Zadanie 12 – czyszczenie starych logów ───────────────────────────────────
@shared_task
def cleanup_old_logs():
    cutoff = timezone.now() - timedelta(days=90)
    deleted_count, _ = LogEntry.objects.filter(created_at__lt=cutoff).delete()
    print(f"Usunięto {deleted_count} starych wpisów logu (starszych niż 90 dni)")
    return deleted_count


# ── Zadanie 13 – web scraping tytułu strony ──────────────────────────────────
@shared_task
def scrape_example_title():
    response = requests.get('https://example.com', timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    title = soup.title.string if soup.title else 'Brak tytułu'
    ScrapedTitle.objects.create(url='https://example.com', title=title)
    print(f"Pobrano tytuł: {title}")
    return title


# ── Zadanie 14 – generowanie raportu CSV ─────────────────────────────────────
@shared_task
def generate_users_csv():
    media_dir = settings.MEDIA_ROOT
    os.makedirs(media_dir, exist_ok=True)
    filename = f"users_report_{timezone.now().strftime('%Y%m%d_%H%M%S')}.csv"
    filepath = media_dir / filename

    users = User.objects.all().values_list('id', 'username', 'email', 'date_joined')
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['ID', 'Nazwa użytkownika', 'Email', 'Data rejestracji'])
        writer.writerows(users)

    print(f"Raport CSV zapisany: {filename}")
    return filename


# ── Zadanie 15 – ponawianie zadania przy błędzie ─────────────────────────────
@shared_task(bind=True, max_retries=3)
def fetch_url_with_retry(self):
    try:
        response = requests.get('http://nieistniejacy-adres.xyz', timeout=5)
        return response.status_code
    except requests.exceptions.RequestException as exc:
        print(f"Błąd połączenia, próba {self.request.retries + 1}/3: {exc}")
        raise self.retry(exc=exc, countdown=60)


# ── Zadanie 16 – klasyfikacja obrazu przez Pillow ────────────────────────────
@shared_task
def classify_image(image_id):
    from PIL import Image as PILImage

    try:
        obj = UploadedImage.objects.get(pk=image_id)
        img_path = settings.MEDIA_ROOT / obj.image.name
        with PILImage.open(img_path) as img:
            width, height = img.size
            mode = img.mode
            is_grayscale = mode in ('L', '1', 'LA')
            result = (
                f"Tryb: {mode} | Wymiary: {width}x{height} px | "
                f"{'Skala szarości' if is_grayscale else 'Kolorowy'}"
            )
        obj.classification_result = result
        obj.save(update_fields=['classification_result'])
        print(f"Klasyfikacja obrazu {image_id}: {result}")
        return result
    except UploadedImage.DoesNotExist:
        print(f"UploadedImage o ID={image_id} nie istnieje")


# ── Zadanie 17 – łańcuch zadań (chain) ───────────────────────────────────────
@shared_task
def generate_random_number():
    import random
    number = random.randint(1, 100)
    print(f"Wygenerowano losową liczbę: {number}")
    return number


@shared_task
def multiply_by_ten(number):
    result = number * 10
    print(f"Wynik mnożenia przez 10: {result}")
    return result


@shared_task
def save_result_to_file(result):
    log_path = settings.BASE_DIR / 'chain_results.txt'
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f"{timezone.now():%Y-%m-%d %H:%M:%S} – wynik łańcucha: {result}\n")
    print(f"Wynik łańcucha zapisany do pliku: {result}")
    return result


def run_chain():
    """Wywołuje łańcuch: generuj → pomnóż × 10 → zapisz do pliku."""
    return chain(
        generate_random_number.s(),
        multiply_by_ten.s(),
        save_result_to_file.s(),
    ).apply_async()


# ── Zadanie 20 – transakcja atomowa + on_commit ───────────────────────────────
@shared_task
def process_new_log_entry(log_entry_id):
    try:
        entry = LogEntry.objects.get(pk=log_entry_id)
        # Symulacja przetwarzania
        time.sleep(1)
        print(f"Przetworzono wpis logu ID={log_entry_id}: {entry.message[:60]}")
    except LogEntry.DoesNotExist:
        print(f"LogEntry o ID={log_entry_id} nie istnieje")
