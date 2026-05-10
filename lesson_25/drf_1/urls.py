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
from django.urls import path, include
from rest_framework import routers
from tasks.views import (TaskViewSet,NoteViewSet, complex_view, PlaceDeleteView, test_celery, multiply, run_task, test_log, log_timestamp, count_users_view, update_user_last_login_view, test_video_task)
from drf_spectacular.views import (
SpectacularAPIView,
SpectacularSwaggerView,
SpectacularRedocView,

)

routers = routers.DefaultRouter()
routers.register(r'tasks', TaskViewSet)
routers.register(r'notes', NoteViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(routers.urls)),
    path("api/auth/", include("djoser.urls")),
    path("api/auth/", include("djoser.urls.jwt")),
    path("__debug__/", include("debug_toolbar.urls")),
    path("api/complex/", complex_view),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),

    path("api/schema/swagger-ui/",SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui",),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"),name="redoc",),
    path("api/places/delete/<int:id>", PlaceDeleteView.as_view()),
    path("test_celery/", test_celery),
    path("run-task/", run_task),
    path("test_log/", test_log),
    path("count-users/", count_users_view),
    path("update-user-last-login/<int:user_id>/", update_user_last_login_view),
    path("process-video/", test_video_task),
]

