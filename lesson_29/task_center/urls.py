from django.urls import path

from .views import (
    count_users_view,
    csv_report_status_view,
    dashboard_view,
    email_notification_view,
    hello_world_view,
    log_timestamp_view,
    multiply_view,
    retry_demo_view,
    scrape_example_view,
    start_chain_view,
    start_csv_report_view,
    start_progress_view,
    task_status_view,
    update_last_login_view,
    upload_image_view,
    video_processing_view,
)

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('hello/', hello_world_view, name='hello-world'),
    path('multiply/', multiply_view, name='multiply'),
    path('log-timestamp/', log_timestamp_view, name='log-timestamp'),
    path('count-users/', count_users_view, name='count-users'),
    path('update-last-login/', update_last_login_view, name='update-last-login'),
    path('video/', video_processing_view, name='video-processing'),
    path('email/', email_notification_view, name='email-notification'),
    path('scrape/', scrape_example_view, name='scrape-example'),
    path('progress/start/', start_progress_view, name='start-progress'),
    path('task-status/<task_id>/', task_status_view, name='task-status'),
    path('reports/start/', start_csv_report_view, name='start-csv-report'),
    path('reports/status/<task_id>/', csv_report_status_view, name='csv-report-status'),
    path('images/upload/', upload_image_view, name='upload-image'),
    path('retry-demo/', retry_demo_view, name='retry-demo'),
    path('chain/', start_chain_view, name='start-chain'),
]