from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from apps.tasks_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Z1-Z5
    path('hello/', views.hello_world_view, name='hello'),
    path('multiply/', views.multiply_view, name='multiply'),
    path('log-timestamp/', views.log_timestamp_view, name='log_timestamp'),
    path('count-users/', views.count_users_view, name='count_users'),
    # Z7
    path('update-last-login/<int:user_id>/', views.update_last_login_view, name='update_last_login'),
    # Z8
    path('process-video/', views.process_video_view, name='process_video'),
    # Z10 + Z20
    path('email-notification/', views.create_email_notification_view, name='create_email_notification'),
    # Z11
    path('start-progress-task/', views.start_progress_task_view, name='start_progress_task'),
    path('task-status/<str:task_id>/', views.task_status_view, name='task_status'),
    # Z14
    path('csv-report/start/', views.start_csv_report_view, name='csv_report_start'),
    path('csv-report/status/<str:task_id>/', views.csv_report_status_view, name='csv_report_status'),
    path('csv-report/download/<str:filename>/', views.csv_report_download_view, name='csv_report_download'),
    # Z15
    path('fetch-unreachable/', views.fetch_unreachable_view, name='fetch_unreachable'),
    # Z16
    path('upload-image/', views.upload_image_view, name='upload_image'),
    # Z17
    path('run-chain/', views.run_chain_view, name='run_chain'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
