from celery.result import AsyncResult
from django.http import JsonResponse
from .models import EmailNotification

from .tasks import hello_world, add_numbers, slow_task, update_user_last_login, process_video, send_email_notification, progress_task


def run_hello_world_task(request):
    task = hello_world.delay()

    return JsonResponse({
        "message": "Task hello_world został wysłany do Celery.",
        "task_id": task.id,
    })


def run_add_numbers_task(request):
    task = add_numbers.delay(5, 7)

    return JsonResponse({
        "message": "Task add_numbers został wysłany do Celery.",
        "task_id": task.id,
        "operation": "5 + 7",
    })


def get_task_result(request, task_id):
    task_result = AsyncResult(task_id)

    return JsonResponse({
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None,
    })

def run_slow_task(request):
    task = slow_task.delay()

    return JsonResponse({
        "message": "Slow task został wysłany do Celery.",
        "task_id": task.id,
    })

def update_user_last_login_view(request, user_id):
    task = update_user_last_login.delay(user_id)

    return JsonResponse({
        "message": f"Update last_login task started for user_id={user_id}",
        "task_id": task.id,
    })

def process_video_view(request):
    task = process_video.delay()

    return JsonResponse({
        "message": "Przetwarzanie wideo rozpoczęte!",
        "task_id": task.id,
    })

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

def start_progress_task_view(request):
    task = progress_task.delay()

    return JsonResponse({
        "message": "Progress task started",
        "task_id": task.id,
    })

def task_status_view(request, task_id):
    task_result = AsyncResult(task_id)

    if task_result.state == "PENDING":
        response = {
            "state": task_result.state,
            "current": 0,
            "total": 100,
            "percent": 0,
            "status": "Pending",
        }

    elif task_result.state == "PROGRESS":
        response = {
            "state": task_result.state,
            "current": task_result.info.get("current", 0),
            "total": task_result.info.get("total", 100),
            "percent": task_result.info.get("percent", 0),
            "status": "In progress",
        }

    elif task_result.state == "SUCCESS":
        response = {
            "state": task_result.state,
            "current": task_result.result.get("current", 100),
            "total": task_result.result.get("total", 100),
            "percent": task_result.result.get("percent", 100),
            "status": task_result.result.get("status", "Completed"),
        }

    else:
        response = {
            "state": task_result.state,
            "current": 0,
            "total": 100,
            "percent": 0,
            "status": str(task_result.info),
        }

    return JsonResponse(response)