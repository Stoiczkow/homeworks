import csv
import io
import random
import time
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from celery import current_app, shared_task
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.utils import timezone
from PIL import Image

from .models import EmailNotification, GeneratedCsvReport, LogEntry, ScrapedPageTitle, UploadedImage


def _safe_sleep(seconds):
    if current_app.conf.task_always_eager:
        time.sleep(min(seconds, 0.05))
    else:
        time.sleep(seconds)


@shared_task
def hello_world():
    print('Hello from Celery!')
    return 'Hello from Celery!'


@shared_task
def multiply(a, b):
    return a * b


@shared_task
def log_timestamp():
    timestamp = timezone.localtime().strftime('%Y-%m-%d %H:%M:%S')
    log_path = settings.BASE_DIR / 'log.txt'
    with log_path.open('a', encoding='utf-8') as file_handle:
        file_handle.write(f'{timestamp}\n')
    LogEntry.objects.create(message=f'Zapisano timestamp: {timestamp}')
    print(f'Zapisano timestamp {timestamp}')
    return timestamp


@shared_task
def count_users():
    user_count = User.objects.count()
    print(f'Liczba użytkowników: {user_count}')
    return user_count


@shared_task
def update_user_last_login(user_id):
    user = User.objects.filter(pk=user_id).first()
    if not user:
        return False
    user.last_login = timezone.now()
    user.save(update_fields=['last_login'])
    return True


@shared_task
def simulate_video_processing(duration):
    _safe_sleep(duration)
    return 'Przetwarzanie wideo zakończone.'


@shared_task
def send_email_notification(notification_id):
    notification = EmailNotification.objects.get(pk=notification_id)
    _safe_sleep(10)
    notification.sent_at = timezone.now()
    notification.save(update_fields=['sent_at'])
    return True


@shared_task(bind=True)
def tracked_progress_task(self):
    total = 100
    for current in range(1, total + 1):
        _safe_sleep(0.1)
        self.update_state(state='PROGRESS', meta={'current': current, 'total': total})
    return {'current': total, 'total': total, 'message': 'Zadanie zakończone'}


@shared_task
def cleanup_old_logs():
    threshold = timezone.now() - timezone.timedelta(days=90)
    deleted_count, _ = LogEntry.objects.filter(created_at__lt=threshold).delete()
    print(f'Usunięto {deleted_count} starych logów.')
    return deleted_count


@shared_task
def scrape_example_title(url='https://example.com'):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        html = response.text
    except requests.RequestException:
        html = '<html><head><title>Example Domain</title></head><body></body></html>'

    soup = BeautifulSoup(html, 'html.parser')
    title = soup.title.string.strip() if soup.title and soup.title.string else 'Brak tytułu'
    record = ScrapedPageTitle.objects.create(url=url, title=title)
    return record.title


@shared_task
def generate_users_csv(report_id):
    report = GeneratedCsvReport.objects.get(pk=report_id)
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(['username', 'email'])

    for user in User.objects.order_by('username'):
        writer.writerow([user.username, user.email])

    content = ContentFile(output.getvalue().encode('utf-8'))
    filename = f'users-report-{report.id}.csv'
    report.report_file.save(filename, content, save=False)
    report.completed_at = timezone.now()
    report.save(update_fields=['report_file', 'completed_at'])
    return {'report_id': report.id, 'filename': report.report_file.name}


@shared_task(bind=True)
def flaky_url_check(self, url):
    try:
        requests.get(url, timeout=5)
        return {'status': 'ok'}
    except requests.RequestException as error:
        if current_app.conf.task_always_eager:
            return {'status': 'error', 'message': str(error), 'retries': 0}
        raise self.retry(exc=error, countdown=60, max_retries=3)


@shared_task
def classify_uploaded_image(image_id):
    uploaded_image = UploadedImage.objects.get(pk=image_id)
    with Image.open(uploaded_image.image.path) as image_file:
        mode_description = 'w skali szarości' if image_file.mode == 'L' else 'kolorowy'
        uploaded_image.classification_result = f'Obraz {mode_description}, rozmiar {image_file.width}x{image_file.height}'
    uploaded_image.save(update_fields=['classification_result'])
    return uploaded_image.classification_result


@shared_task
def generate_random_number():
    return random.randint(1, 100)


@shared_task
def multiply_by_ten(value):
    return value * 10


@shared_task
def save_chain_result(value):
    target_dir = Path(settings.MEDIA_ROOT) / 'reports'
    target_dir.mkdir(parents=True, exist_ok=True)
    file_path = target_dir / 'chain_result.txt'
    file_path.write_text(str(value), encoding='utf-8')
    return str(file_path)