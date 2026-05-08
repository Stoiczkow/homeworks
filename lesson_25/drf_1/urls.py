"""
URL configuration for drf_1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

from tasks.views import (
    AuthorViewSet,
    BookViewSet,
    NoteViewSet,
    ProductViewSet,
    ProtectedUserView,
    TaskViewSet,
    calculate,
    celery_chain,
    celery_fail_retry,
    celery_generate_report,
    celery_hello,
    celery_log_timestamp,
    celery_multiply,
    celery_priority_email,
    celery_process_video,
    celery_progress,
    celery_send_email,
    celery_update_login,
    classify_image,
    create_user_transaction,
    download_report,
    expensive_stats,
    hello,
    report_status,
    set_name,
    task_status,
    test_celery,
)

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'products', ProductViewSet)
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),

    path("__debug__/", include("debug_toolbar.urls")),

    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),

    path("test_celery/", test_celery),
    path("api/hello/", hello),
    path("api/set-name/", set_name),
    path("api/calculate/", calculate),
    path("api/protected/", ProtectedUserView.as_view()),
    path("api/expensive-stats/", expensive_stats),
    path("api/celery/hello/", celery_hello),
    path("api/celery/multiply/", celery_multiply),
    path("api/celery/log-timestamp/", celery_log_timestamp),
    path("api/celery/update-login/", celery_update_login),
    path("api/celery/process-video/", celery_process_video),
    path("api/celery/send-email/", celery_send_email),
    path("api/celery/progress/", celery_progress),
    path("api/celery/fail-retry/", celery_fail_retry),
    path("api/celery/chain/", celery_chain),
    path("api/celery/priority-email/", celery_priority_email),
    path("api/celery/create-user-transaction/", create_user_transaction),
    path("api/task-status/<str:task_id>/", task_status),
    path("api/reports/generate/", celery_generate_report),
    path("api/reports/<int:report_id>/", report_status),
    path("api/reports/<int:report_id>/download/", download_report),
    path("api/images/classify/", classify_image),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
