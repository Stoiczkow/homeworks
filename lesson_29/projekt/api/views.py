from celery.result import AsyncResult
from django.db import transaction
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .models import EmailNotification, LogEntry, UploadedImage
from .tasks import (
    fetch_url_with_retry,
    generate_users_csv,
    long_task_with_progress,
    process_new_log_entry,
    process_video,
    run_chain,
    send_notification_email,
    classify_image,
)


# ── Zadanie 8 – uruchomienie symulacji przetwarzania wideo ───────────────────
def start_video_processing(request):
    process_video.delay()
    return JsonResponse({'message': 'Przetwarzanie wideo rozpoczęte!'})


# ── Zadanie 11 – uruchomienie zadania z postępem + sprawdzenie statusu ───────
def start_long_task(request):
    task = long_task_with_progress.delay()
    return JsonResponse({'task_id': task.id, 'status': 'uruchomiono'})


def task_status(request, task_id):
    result = AsyncResult(task_id)
    if result.state == 'PROGRESS':
        data = {
            'state': result.state,
            'current': result.info.get('current', 0),
            'total': result.info.get('total', 100),
            'percent': result.info.get('percent', 0),
        }
    elif result.state == 'SUCCESS':
        data = {'state': result.state, 'result': result.result}
    elif result.state == 'FAILURE':
        data = {'state': result.state, 'error': str(result.info)}
    else:
        data = {'state': result.state}
    return JsonResponse(data)


# ── Zadanie 14 – generowanie CSV i sprawdzanie statusu ───────────────────────
def start_csv_generation(request):
    task = generate_users_csv.delay()
    return JsonResponse({'task_id': task.id, 'message': 'Generowanie raportu CSV rozpoczęte'})


def csv_task_status(request, task_id):
    result = AsyncResult(task_id)
    if result.state == 'SUCCESS':
        filename = result.result
        download_url = f"{request.scheme}://{request.get_host()}/media/{filename}"
        return JsonResponse({'state': result.state, 'download_url': download_url})
    return JsonResponse({'state': result.state})


# ── Zadanie 15 – uruchomienie zadania z ponowieniem przy błędzie ─────────────
def start_fetch_with_retry(request):
    task = fetch_url_with_retry.delay()
    return JsonResponse({'task_id': task.id, 'message': 'Zadanie uruchomione, 3 próby przy błędzie'})


# ── Zadanie 16 – przesyłanie i klasyfikacja obrazu ───────────────────────────
@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        obj = UploadedImage.objects.create(image=request.FILES['image'])
        classify_image.delay(obj.pk)
        return JsonResponse({
            'image_id': obj.pk,
            'message': 'Obraz przesłany, klasyfikacja w toku...',
        })
    return JsonResponse({'error': 'Prześlij plik w polu "image" metodą POST'}, status=400)


def image_classification_result(request, image_id):
    try:
        obj = UploadedImage.objects.get(pk=image_id)
        return JsonResponse({
            'image_id': obj.pk,
            'classification_result': obj.classification_result or 'W trakcie przetwarzania...',
        })
    except UploadedImage.DoesNotExist:
        return JsonResponse({'error': 'Nie znaleziono obrazu'}, status=404)


# ── Zadanie 17 – uruchomienie łańcucha zadań ─────────────────────────────────
def start_chain(request):
    task = run_chain()
    return JsonResponse({'task_id': task.id, 'message': 'Łańcuch zadań uruchomiony'})


# ── Zadanie 10 – tworzenie i wysyłanie powiadomienia (priority_queue) ────────
@csrf_exempt
def send_email_notification(request):
    if request.method == 'POST':
        notification = EmailNotification.objects.create(
            recipient_email=request.POST.get('email', 'test@example.com'),
            subject=request.POST.get('subject', 'Test'),
            body=request.POST.get('body', 'Treść wiadomości'),
        )
        send_notification_email.apply_async(
            args=[notification.pk],
            queue='priority_queue',
        )
        return JsonResponse({'notification_id': notification.pk, 'message': 'Mail w kolejce'})
    return JsonResponse({'error': 'Użyj metody POST'}, status=400)


# ── Zadanie 20 – transakcja atomowa + on_commit ───────────────────────────────
@csrf_exempt
def create_log_entry(request):
    if request.method == 'POST':
        message = request.POST.get('message', 'Testowy wpis logu')
        with transaction.atomic():
            entry = LogEntry.objects.create(message=message)
            # on_commit zapewnia, że zadanie Celery uruchomi się dopiero po
            # pomyślnym zatwierdzeniu transakcji – obiekt na pewno istnieje w bazie
            transaction.on_commit(lambda: process_new_log_entry.delay(entry.pk))
        return JsonResponse({'entry_id': entry.pk, 'message': 'Wpis logu utworzony, zadanie w kolejce'})
    return JsonResponse({'error': 'Użyj metody POST'}, status=400)
