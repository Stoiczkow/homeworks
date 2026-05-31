"""
URL configuration for project project.

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
from tasks import views



router = routers.DefaultRouter()

router.register(r"products", views.ProductViewSet)
router.register(r"notes", views.NoteViewSet)
router.register(r"book", views.BookViewSet)
router.register(r"author", views.AuthorViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),


    path('api/', include(router.urls)),
    # path('api/', include(router.urls)),
    path('api/hello/', views.helloview, name="hello-view"),
    path('api/set-name/', views.setName, name='set-Name'),
    path('api/auth/', include('djoser.urls')),
    path('api/auth/', include('djoser.urls.jwt')),
    path("test_celery/", views.test_celery),
    path("hello_world/", views.test_hello_world),#task1
    path("multiply/", views.test_multiply),#task2
    path("test_time/", views.test_time), #task3
    path("count_user/", views.test_count_user), #test4
    path("update_last_login/", views.test_update_user_last_login),#test7
    path("video_processing_simulation/", views.test_video_processing_simulation), #test8
    path("email_notification/",  views.test_EmailNotification),#test10
    path("clear_log/", views.test_log_Entry)#12
]


