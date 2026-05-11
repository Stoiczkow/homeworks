"""Zadania Celery dla aplikacji lesson_29."""
import csv
import random
import time
from datetime import datetime, timedelta

import requests
from bs4 import BeautifulSoup
from celery import shared_task
from django.conf import settings
from django.utils import timezone


# Zadanie 1: Pierwsze zadanie
@shared_task
def hello_world():
    print("Hello from Celery!")


# Zadanie 2: mnozenie dwoch liczb w tle
@shared_task
def multiply(a, b):
    result = a * b
    print(f"multiply({a}, {b}) = {result}")
    return result


# Zadanie 3: dopisanie aktualnego czasu do log.txt
@shared_task
def log_timestamp():
    now = datetime.now().isoformat(timespec='seconds')
    log_path = settings.BASE_DIR / 'log.txt'
    with open(log_path, 'a', encoding='utf-8') as f:
        f.write(f'{now}\n')
    print(f"log_timestamp: dopisano {now} do {log_path.name}")
    return now


# Zadanie 5: zliczenie uzytkownikow w bazie
@shared_task
def count_users():
    from django.contrib.auth import get_user_model
    User = get_user_model()
    count = User.objects.count()
    print(f"count_users: w bazie jest {count} uzytkownik(ow)")
    return count


# Zadanie 7: aktualizacja last_login uzytkownika po ID
@shared_task
def update_user_last_login(user_id):
    from django.contrib.auth import get_user_model
    User = get_user_model()
    try:
        user = User.objects.get(pk=user_id)
    except User.DoesNotExist:
        print(f"update_user_last_login: user id={user_id} nie istnieje")
        return None
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
    print(f"update_user_last_login: user={user.username} last_login={user.last_login}")
    return user.last_login.isoformat()


# Zadanie 8: symulacja przetwarzania wideo (15s)
@shared_task
def process_video():
    print("process_video: start")
    time.sleep(15)
    print("process_video: koniec")
    return "Wideo przetworzone."


# Zadanie 10: wysylka maila (symulacja) z aktualizacja sent_at
@shared_task
def send_email_notification(notification_id):
    from apps.tasks_app.models import EmailNotification
    try:
        notification = EmailNotification.objects.get(pk=notification_id)
    except EmailNotification.DoesNotExist:
        print(f"send_email_notification: brak EmailNotification id={notification_id}")
        return None
    print(f"send_email_notification: 'wysylam' do {notification.recipient_email}...")
    time.sleep(5)  # symulacja SMTP
    notification.sent_at = timezone.now()
    notification.save(update_fields=['sent_at'])
    print(f"send_email_notification: id={notification_id} sent_at={notification.sent_at}")
    return notification.sent_at.isoformat()


# Zadanie 11: zadanie z postepem - aktualizacja stanu w trakcie wykonania
@shared_task(bind=True)
def long_running_progress_task(self):
    total = 100
    for i in range(1, total + 1):
        time.sleep(0.1)
        self.update_state(
            state='PROGRESS',
            meta={'current': i, 'total': total, 'percent': i},
        )
    return {'current': total, 'total': total, 'percent': 100, 'status': 'done'}


# Zadanie 12: usuwanie LogEntry starszych niz 90 dni
@shared_task
def cleanup_old_log_entries():
    from apps.tasks_app.models import LogEntry
    cutoff = timezone.now() - timedelta(days=90)
    deleted_count, _ = LogEntry.objects.filter(created_at__lt=cutoff).delete()
    print(f"cleanup_old_log_entries: usunieto {deleted_count} wpis(ow) starszych niz 90 dni")
    return deleted_count


# Zadanie 13: web scraping example.com i zapis tytulu w bazie
@shared_task
def scrape_example_com():
    from apps.tasks_app.models import ScrapedPage
    url = 'https://example.com'
    response = requests.get(url, timeout=10)
    soup = BeautifulSoup(response.text, 'html.parser')
    title_tag = soup.find('title')
    title = title_tag.get_text(strip=True) if title_tag else '(brak tytulu)'
    page = ScrapedPage.objects.create(url=url, title=title)
    print(f"scrape_example_com: zapisano '{title}' (id={page.pk})")
    return page.pk


# Zadanie 14: generowanie raportu CSV z uzytkownikami
@shared_task
def generate_users_csv():
    from django.contrib.auth import get_user_model
    User = get_user_model()

    media_root = settings.MEDIA_ROOT
    media_root.mkdir(parents=True, exist_ok=True)
    filename = f"users_{datetime.now():%Y%m%d_%H%M%S}.csv"
    filepath = media_root / filename

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['id', 'username', 'email'])
        for user in User.objects.all().iterator():
            writer.writerow([user.pk, user.username, user.email])

    # Symulacja "ciezkiej" operacji - dla zadania o sledzenie statusu.
    time.sleep(3)
    print(f"generate_users_csv: zapisano raport do {filepath}")
    # Zwracamy relatywna sciezke wzgledem MEDIA_ROOT - widok zbuduje z tego URL.
    return filename


# Zadanie 15: zadanie z retry przy bledzie polaczenia
@shared_task(bind=True, max_retries=3)
def fetch_unreachable_url(self):
    url = 'http://nieistniejaca-domena-12345.example'
    try:
        response = requests.get(url, timeout=5)
        return response.status_code
    except requests.RequestException as exc:
        print(f"fetch_unreachable_url: blad {exc!r}, retry {self.request.retries + 1}/3")
        # countdown=60 -> ponow za 60 sekund
        raise self.retry(exc=exc, countdown=60, max_retries=3)


# Zadanie 16: klasyfikacja obrazu przez Pillow
@shared_task
def classify_image(image_id):
    from PIL import Image
    from apps.tasks_app.models import UploadedImage
    try:
        uploaded = UploadedImage.objects.get(pk=image_id)
    except UploadedImage.DoesNotExist:
        print(f"classify_image: brak UploadedImage id={image_id}")
        return None

    with Image.open(uploaded.image.path) as img:
        mode = img.mode
        width, height = img.size
        color_label = 'skala szarosci' if mode in ('L', 'LA', '1') else 'kolorowy'
        result = f'{color_label}; tryb={mode}; wymiary={width}x{height}'

    uploaded.classification_result = result
    uploaded.save(update_fields=['classification_result'])
    print(f"classify_image: id={image_id} -> {result}")
    return result


# Zadanie 17: chain - trzy zadania w lancuchu
@shared_task
def generate_random_number():
    n = random.randint(1, 100)
    print(f"generate_random_number: {n}")
    return n


@shared_task
def multiply_by_ten(value):
    result = value * 10
    print(f"multiply_by_ten: {value} -> {result}")
    return result


@shared_task
def save_to_file(value):
    path = settings.BASE_DIR / 'chain_result.txt'
    with open(path, 'a', encoding='utf-8') as f:
        f.write(f"{datetime.now().isoformat(timespec='seconds')}: {value}\n")
    print(f"save_to_file: zapisano {value} do {path.name}")
    return str(path)


# Zadanie 18: krytyczny mail kierowany do priority_queue (przez routing w settings.py)
@shared_task
def send_critical_email(recipient_email, subject, body):
    print(f"send_critical_email[priority_queue]: wysylam do {recipient_email} temat='{subject}'")
    time.sleep(2)
    print(f"send_critical_email: wyslane (body length={len(body)})")
    return True