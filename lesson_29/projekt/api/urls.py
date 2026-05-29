from django.urls import path
from . import views

urlpatterns = [
    # Zadanie 8 – symulacja przetwarzania wideo
    path('start-video/', views.start_video_processing, name='start-video'),

    # Zadanie 10 – powiadomienie email przez priority_queue
    path('send-email/', views.send_email_notification, name='send-email'),

    # Zadanie 11 – śledzenie postępu zadania
    path('start-long-task/', views.start_long_task, name='start-long-task'),
    path('task-status/<str:task_id>/', views.task_status, name='task-status'),

    # Zadanie 14 – generowanie raportu CSV
    path('generate-csv/', views.start_csv_generation, name='generate-csv'),
    path('csv-status/<str:task_id>/', views.csv_task_status, name='csv-status'),

    # Zadanie 15 – zadanie z ponowieniem
    path('fetch-url/', views.start_fetch_with_retry, name='fetch-url'),

    # Zadanie 16 – przesyłanie i klasyfikacja obrazu
    path('upload-image/', views.upload_image, name='upload-image'),
    path('image-result/<int:image_id>/', views.image_classification_result, name='image-result'),

    # Zadanie 17 – łańcuch zadań
    path('start-chain/', views.start_chain, name='start-chain'),

    # Zadanie 20 – transakcja atomowa + on_commit
    path('create-log/', views.create_log_entry, name='create-log'),
]
