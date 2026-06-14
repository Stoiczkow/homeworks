from django.urls import path

from . import views

app_name = "jobs"

urlpatterns = [
    path("hello/", views.run_hello_world_task, name="run_hello_world_task"),
    path("add/", views.run_add_numbers_task, name="run_add_numbers_task"),
    path("result/<str:task_id>/", views.get_task_result, name="get_task_result"),
    path("slow/", views.run_slow_task, name="run_slow_task"),
    path(
    "update-last-login/<int:user_id>/",
    views.update_user_last_login_view,
    name="update_user_last_login"),
    path("process-video/", views.process_video_view, name="process_video"),
    path("send-test-email/", views.send_test_email_view, name="send_test_email"),
    path("progress-task/", views.start_progress_task_view, name="progress_task"),
    path("task-status/<str:task_id>/", views.task_status_view, name="task_status"),
]