import time
from celery import shared_task
from pathlib import Path
from django.http import JsonResponse
from django.conf import settings
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth import get_user_model
from .models import EmailNotification, LogEntry
@shared_task
def hello_world():
    print("Hello from Celery!")
    return "Hello from Celery!"


@shared_task
def add_numbers(a, b):
    result = a + b
    print(f"Wynik dodawania: {a} + {b} = {result}")
    return result


@shared_task
def slow_task():
    print("Slow task started...")
    time.sleep(10)
    print("Slow task finished!")
    return "Slow task completed after 10 seconds"

@shared_task
def log_timestamp():
    current_time = timezone.localtime(timezone.now())
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    log_file_path = Path(settings.BASE_DIR) / "log.txt"

    with open(log_file_path, "a", encoding="utf-8") as file:
        file.write(f"{formatted_time}\n")

    print(f"Zapisano czas do log.txt: {formatted_time}")

    return formatted_time

@shared_task
def count_users():
    User = get_user_model()
    users_count = User.objects.count()

    print(f"Liczba użytkowników w bazie: {users_count}")

    return users_count

@shared_task
def update_user_last_login(user_id):
    User = get_user_model()

    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        message = f"User with id={user_id} does not exist"
        print(message)
        return message

    user.last_login = timezone.now()
    user.save(update_fields=["last_login"])

    message = f"Updated last_login for user: {user.username}"
    print(message)
    return message

@shared_task
def process_video():
    print("Rozpoczynam przetwarzanie wideo...")
    time.sleep(15)
    print("Przetwarzanie wideo zakończone.")
    return "Video processed successfully"

@shared_task
def multiply(a, b):
    result = a * b
    print(f"{a} * {b} = {result}")
    return result

@shared_task
def send_email_notification(notification_id):
    try:
        notification = EmailNotification.objects.get(id=notification_id)
    except EmailNotification.DoesNotExist:
        message = f"EmailNotification with id={notification_id} does not exist"
        print(message)
        return message

    print(f"Sending email to {notification.recipient_email}...")
    print(f"Subject: {notification.subject}")
    print(f"Body: {notification.body}")

    time.sleep(5)

    notification.sent_at = timezone.now()
    notification.save(update_fields=["sent_at"])

    message = f"Email notification {notification.id} sent successfully"
    print(message)
    return message


def send_test_email_view(request):
    notification = EmailNotification.objects.create(
        recipient_email="test@example.com",
        subject="Test Celery email",
        body="To jest testowa wiadomość wysłana przez task Celery.",
    )

    task = send_email_notification.delay(notification.id)

    return JsonResponse({
        "message": "Email notification task started",
        "notification_id": notification.id,
        "task_id": task.id,
    })

@shared_task
def send_email_notification(notification_id):
    try:
        notification = EmailNotification.objects.get(id=notification_id)
    except EmailNotification.DoesNotExist:
        message = f"EmailNotification with id={notification_id} does not exist"
        print(message)
        return message

    print(f"Sending email to {notification.recipient_email}...")
    print(f"Subject: {notification.subject}")
    print(f"Body: {notification.body}")

    time.sleep(5)

    notification.sent_at = timezone.now()
    notification.save(update_fields=["sent_at"])

    message = f"Email notification {notification.id} sent successfully"
    print(message)
    return message

@shared_task(bind=True)
def progress_task(self):
    total = 100

    for i in range(1, total + 1):
        time.sleep(0.1)

        self.update_state(
            state="PROGRESS",
            meta={
                "current": i,
                "total": total,
                "percent": i,
            }
        )

    return {
        "current": total,
        "total": total,
        "percent": 100,
        "status": "Task completed",
    }
@shared_task
def cleanup_old_log_entries():
    cutoff_date = timezone.now() - timedelta(days=90)

    deleted_count, _ = LogEntry.objects.filter(
        created_at__lt=cutoff_date
    ).delete()

    message = f"Deleted {deleted_count} old log entries"
    print(message)
    return message