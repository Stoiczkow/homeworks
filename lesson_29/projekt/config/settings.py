from pathlib import Path
from celery.schedules import crontab

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-lesson29-celery-secret-key'

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'api',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'pl'
TIME_ZONE = 'Europe/Warsaw'
USE_I18N = True
USE_TZ = True

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Celery ──────────────────────────────────────────────────────────────────
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Europe/Warsaw'

# Zadanie 18 – konfiguracja dwóch kolejek: default i priority_queue
CELERY_TASK_ROUTES = {
    'api.tasks.send_notification_email': {'queue': 'priority_queue'},
}

# Zadanie 4 + 6 + 12 + 13 – harmonogramy Celery Beat
CELERY_BEAT_SCHEDULE = {
    # Zadanie 4 – log_timestamp co 10 sekund
    'log-timestamp-every-10s': {
        'task': 'api.tasks.log_timestamp',
        'schedule': 10.0,
    },
    # Zadanie 6 – count_users codziennie o 23:00
    'count-users-daily-23': {
        'task': 'api.tasks.count_users',
        'schedule': crontab(hour=23, minute=0),
    },
    # Zadanie 12 – cleanup_old_logs raz dziennie o 2:00
    'cleanup-old-logs-daily': {
        'task': 'api.tasks.cleanup_old_logs',
        'schedule': crontab(hour=2, minute=0),
    },
    # Zadanie 13 – scrape_example_title co godzinę
    'scrape-example-title-hourly': {
        'task': 'api.tasks.scrape_example_title',
        'schedule': crontab(minute=0),
    },
}

# Uruchamianie:
# celery -A config worker -l info -Q default
# celery -A config worker -l info -Q priority_queue  (zadanie 18)
# celery -A config beat -l info                       (harmonogram)
# celery -A config flower                             (zadanie 19 – Flower UI na :5555)
