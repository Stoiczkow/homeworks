"""Konfiguracja Celery dla projektu lesson_29."""
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings.settings')

app = Celery('lesson_29')

# Wczytaj konfiguracje z settings.py - wszystkie ustawienia z prefixem CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatyczne wyszukanie tasks.py w zainstalowanych aplikacjach.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')