from celery import chain
from celery.result import AsyncResult
from django.conf import settings
from django.db import transaction
from django.http import FileResponse, Http404, JsonResponse
from django.shortcuts import render
from django.urls import reverse

from apps.tasks_app.models import EmailNotification, UploadedImage
from apps.tasks_app.tasks import (
    classify_image,
    count_users,
    fetch_unreachable_url,
    generate_random_number,
    generate_users_csv,
    hello_world,
    log_timestamp,
    long_running_progress_task,
    multiply,
    multiply_by_ten,
    process_video,
    save_to_file,
    send_email_notification,
    update_user_last_login,
)


# Zadanie 1: widok wywolujacy hello_world w tle
def hello_world_view(request):
    task = hello_world.delay()
    return JsonResponse({
        "message": "Zadanie hello_world wystartowane w tle.",
        "task_id": task.id,
    })


# Zadanie 3: recznie odpalany trigger log_timestamp (Z4 odpali to przez Beat)
def log_timestamp_view(request):
    task = log_timestamp.delay()
    return JsonResponse({
        "message": "Dopisano timestamp do log.txt.",
        "task_id": task.id,
    })


# Zadanie 5: recznie odpalany trigger count_users (Z6 odpali to przez Beat o 23:00)
def count_users_view(request):
    task = count_users.delay()
    return JsonResponse({
        "message": "Zadanie count_users wystartowane w tle.",
        "task_id": task.id,
    })


# Zadanie 2: formularz HTML + wywolanie multiply
def multiply_view(request):
    context = {}
    if request.method == 'POST':
        try:
            a = float(request.POST.get('a', ''))
            b = float(request.POST.get('b', ''))
        except ValueError:
            context['error'] = 'Wpisz dwie liczby.'
            return render(request, 'tasks_app/multiply.html', context)

        async_result = multiply.delay(a, b)
        # Czekamy max 5s na wynik - dla nauki, w produkcji raczej nie blokuj.
        try:
            result = async_result.get(timeout=5)
        except Exception as exc:
            context['error'] = f'Timeout lub blad: {exc}'
            context.update({'task_id': async_result.id, 'a': a, 'b': b})
            return render(request, 'tasks_app/multiply.html', context)

        context.update({
            'a': a, 'b': b,
            'task_id': async_result.id,
            'result': result,
        })
    return render(request, 'tasks_app/multiply.html', context)


# Zadanie 7: GET /update-last-login/<user_id>/
def update_last_login_view(request, user_id):
    task = update_user_last_login.delay(user_id)
    return JsonResponse({
        "message": f"Zadanie update_user_last_login dla user_id={user_id} w kolejce.",
        "task_id": task.id,
    })


# Zadanie 8: natychmiastowa odpowiedz, wideo "przetwarza sie" w tle
def process_video_view(request):
    task = process_video.delay()
    return JsonResponse({
        "message": "Przetwarzanie wideo rozpoczęte!",
        "task_id": task.id,
    })


# Zadanie 10 + 20: tworzenie EmailNotification w transakcji + on_commit
def create_email_notification_view(request):
    """
    Z20: zadanie wywolujemy dopiero po pomyslnym commit transakcji.
    Gdyby zadanie poszlo do kolejki przed commit, worker moglby wystartowac
    zanim INSERT bedzie widoczny -> EmailNotification.DoesNotExist.
    """
    with transaction.atomic():
        notification = EmailNotification.objects.create(
            recipient_email='test@example.com',
            subject='Powitanie',
            body='Witaj w naszym serwisie!',
        )
        transaction.on_commit(
            lambda: send_email_notification.delay(notification.pk)
        )
    return JsonResponse({
        "message": "EmailNotification utworzony, wysylka w tle po commit.",
        "notification_id": notification.pk,
    })


# Zadanie 11: start zadania + endpoint do sprawdzania statusu
def start_progress_task_view(request):
    task = long_running_progress_task.delay()
    return JsonResponse({
        "message": "Long-running task wystartowal.",
        "task_id": task.id,
        "status_url": reverse('task_status', args=[task.id]),
    })


def task_status_view(request, task_id):
    result = AsyncResult(task_id)
    payload = {
        "task_id": task_id,
        "state": result.state,
    }
    if result.state == 'PROGRESS':
        payload["progress"] = result.info  # {'current', 'total', 'percent'}
    elif result.state == 'SUCCESS':
        payload["result"] = result.result
    elif result.state == 'FAILURE':
        payload["error"] = str(result.info)
    return JsonResponse(payload)


# Zadanie 14: start generowania CSV + sprawdzenie statusu + pobranie pliku
def start_csv_report_view(request):
    task = generate_users_csv.delay()
    return JsonResponse({
        "message": "Generowanie CSV wystartowalo.",
        "task_id": task.id,
        "status_url": reverse('csv_report_status', args=[task.id]),
    })


def csv_report_status_view(request, task_id):
    result = AsyncResult(task_id)
    payload = {"task_id": task_id, "state": result.state}
    if result.state == 'SUCCESS':
        filename = result.result
        payload["download_url"] = reverse('csv_report_download', args=[filename])
    elif result.state == 'FAILURE':
        payload["error"] = str(result.info)
    return JsonResponse(payload)


def csv_report_download_view(request, filename):
    # Tylko CSV z MEDIA_ROOT, bez dziurkowania w katalogi.
    if '/' in filename or '\\' in filename or not filename.endswith('.csv'):
        raise Http404('Nieprawidlowa nazwa pliku.')
    filepath = settings.MEDIA_ROOT / filename
    if not filepath.exists():
        raise Http404('Plik nie istnieje.')
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename=filename)


# Zadanie 15: trigger zadania z retry
def fetch_unreachable_view(request):
    task = fetch_unreachable_url.delay()
    return JsonResponse({
        "message": "fetch_unreachable_url wystartowane (3 retry co 60s).",
        "task_id": task.id,
    })


# Zadanie 16: prosty formularz uploadu obrazka
def upload_image_view(request):
    context = {}
    if request.method == 'POST' and request.FILES.get('image'):
        uploaded = UploadedImage.objects.create(image=request.FILES['image'])
        task = classify_image.delay(uploaded.pk)
        context.update({
            'uploaded_id': uploaded.pk,
            'task_id': task.id,
            'image_url': uploaded.image.url,
        })
    return render(request, 'tasks_app/upload_image.html', context)


# Zadanie 17: chain trzech zadan
def run_chain_view(request):
    workflow = chain(
        generate_random_number.s(),
        multiply_by_ten.s(),
        save_to_file.s(),
    )
    async_result = workflow.apply_async()
    return JsonResponse({
        "message": "Chain wystartowal (random -> *10 -> file).",
        "task_id": async_result.id,
    })
