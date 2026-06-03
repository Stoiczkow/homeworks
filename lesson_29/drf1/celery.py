import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf1.settings")

app = Celery("drf1")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()