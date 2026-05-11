"""Django settings for lesson_29 - Celery."""
import os
from pathlib import Path
from celery.schedules import crontab
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv(
    'SECRET_KEY',
    'django-insecure-lesson29-celery-demo-key-change-me'
)
DEBUG = os.getenv('DEBUG', 'True') == 'True'
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_celery_beat',
    'apps.tasks_app',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Celery configuration
# Redis z lesson_27 (port 6379). Uzywamy DB 2 (broker) i DB 3 (results),
# zeby nie kolidowac z django cache (DB 1).
CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://127.0.0.1:6379/2')
CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://127.0.0.1:6379/3')
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Warsaw'

# Zadanie 4 + 6 + 12 + 13: harmonogram zadan dla Celery Beat
CELERY_BEAT_SCHEDULE = {
    # Z4: co 10 sekund dopisuj timestamp do log.txt
    'log-timestamp-every-10s': {
        'task': 'apps.tasks_app.tasks.log_timestamp',
        'schedule': 10.0,
    },
    # Z6: codziennie o 23:00 zliczaj uzytkownikow
    'count-users-daily-23-00': {
        'task': 'apps.tasks_app.tasks.count_users',
        'schedule': crontab(hour=23, minute=0),
    },
    # Z12: codziennie o 03:00 usuwaj LogEntry starsze niz 90 dni
    'cleanup-old-log-entries-daily': {
        'task': 'apps.tasks_app.tasks.cleanup_old_log_entries',
        'schedule': crontab(hour=3, minute=0),
    },
    # Z13: co godzine pobieraj tytul strony example.com
    'scrape-example-com-hourly': {
        'task': 'apps.tasks_app.tasks.scrape_example_com',
        'schedule': crontab(minute=0),
    },
}

# Z18: dwie kolejki - default i priority_queue.
# Krytyczne zadania (send_critical_email) zawsze ida do priority_queue.
CELERY_TASK_DEFAULT_QUEUE = 'default'
CELERY_TASK_ROUTES = {
    'apps.tasks_app.tasks.send_critical_email': {'queue': 'priority_queue'},
}
