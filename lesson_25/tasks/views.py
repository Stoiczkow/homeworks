from celery import chain
from celery.result import AsyncResult
from django.conf import settings
from django.contrib.auth.models import User
from django.core.cache import cache
from django.db import transaction
from django.http import FileResponse, Http404
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes

from .models import (
    Author,
    Book,
    EmailNotification,
    Product,
    Task,
    UploadedImage,
    UserReport,
)
from .serializers import (
    AuthorSerializer,
    BookSerializer,
    NoteSerializer,
    ProductSerializer,
    TaskSerializer,
)
from .tasks import (
    classify_uploaded_image,
    critical_email_task,
    failing_url_task,
    generate_random_number,
    generate_users_csv,
    hello_world,
    log_timestamp,
    multiply,
    multiply_by_ten,
    process_video,
    progress_task,
    save_chain_result,
    send_email_notification,
    simulate_cpu_bound_task,
    update_user_last_login,
)

class TaskViewSet(viewsets.ModelViewSet):
    """
        Widok obsługje cału CRUD
    """
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

    @extend_schema(
        summary="Pobierz szczegóły jednego produktu",
        description="Zwraca pełne informacje o produkcie na podstawie jego ID.",
        tags=["Tasks"], # Grupuje endpointy w UI
    )

    @method_decorator(cache_page(60 * 10, key_prefix='tasks-list'))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @method_decorator(cache_page(60, key_prefix='tasks-detail'))
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    def perform_update(self, serializer):
        serializer.save()
        cache.clear()

    def perform_destroy(self, instance):
        instance.delete()
        cache.clear()


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        min_price = self.request.query_params.get("min_price")
        max_price = self.request.query_params.get("max_price")

        if min_price:
            queryset = queryset.filter(price__gte=min_price)
        if max_price:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.none()
    serializer_class = NoteSerializer

    def get_queryset(self):
        from .models import Note

        return Note.objects.all().order_by("-created_at")


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all().order_by("name")
    serializer_class = AuthorSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.select_related("author").all().order_by("title")
    serializer_class = BookSerializer


class ProtectedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"username": request.user.username})


@api_view(["GET"])
def test_celery(request):
    task = simulate_cpu_bound_task.delay(20)
    return Response(
        {"message": "Zadanie jest w trakcie wykonywania", "task_id": task.id}
    )


@api_view(["GET"])
def set_name(request):
    name = request.GET.get("name", "")
    response = Response({"message": f"Cookie ustawione dla: {name or 'Gość'}"})
    if name:
        response.set_cookie("user_name", name)
    return response


@api_view(["GET"])
def hello(request):
    name = request.COOKIES.get("user_name", "Gość")
    return Response({"message": f"Witaj, {name}!"})


@api_view(["GET"])
def calculate(request):
    try:
        num1 = float(request.GET["num1"])
        num2 = float(request.GET["num2"])
    except (KeyError, ValueError):
        return Response({"error": "Podaj poprawne num1 i num2."}, status=400)

    operation = request.GET.get("operation")
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return Response({"error": "Nie można dzielić przez zero."}, status=400)
        result = num1 / num2
    else:
        return Response({"error": "Niepoprawna operacja."}, status=400)

    return Response({"result": result})


@api_view(["GET"])
def expensive_stats(request):
    import time

    cached_value = cache.get("expensive_stats")
    if cached_value is None:
        time.sleep(3)
        cached_value = "wynik skomplikowanych obliczeń"
        cache.set("expensive_stats", cached_value, 60)

    return Response({"task_count": Task.objects.count(), "expensive": cached_value})


@api_view(["GET"])
def celery_hello(request):
    task = hello_world.delay()
    return Response({"task_id": task.id})


@api_view(["GET", "POST"])
def celery_multiply(request):
    data = request.data if request.method == "POST" else request.GET
    a = int(data.get("a", 1))
    b = int(data.get("b", 1))
    task = multiply.delay(a, b)
    return Response({"task_id": task.id, "a": a, "b": b})


@api_view(["GET"])
def celery_log_timestamp(request):
    task = log_timestamp.delay()
    return Response({"task_id": task.id})


@api_view(["POST"])
def celery_update_login(request):
    user_id = request.data.get("user_id")
    task = update_user_last_login.delay(user_id)
    return Response({"task_id": task.id})


@api_view(["POST"])
def celery_process_video(request):
    task = process_video.delay()
    return Response({"message": "Przetwarzanie wideo rozpoczęte!", "task_id": task.id})


@api_view(["POST"])
def celery_send_email(request):
    notification = EmailNotification.objects.create(
        recipient_email=request.data.get("recipient_email", "user@example.com"),
        subject=request.data.get("subject", "Test"),
        body=request.data.get("body", "Treść wiadomości"),
    )
    task = send_email_notification.delay(notification.id)
    return Response({"notification_id": notification.id, "task_id": task.id})


@api_view(["POST"])
def celery_progress(request):
    task = progress_task.delay()
    return Response({"task_id": task.id})


@api_view(["GET"])
def task_status(request, task_id):
    result = AsyncResult(task_id)
    return Response({"state": result.state, "meta": result.info or {}})


@api_view(["POST"])
def celery_generate_report(request):
    report = UserReport.objects.create()
    task = generate_users_csv.delay(report.id)
    return Response({"report_id": report.id, "task_id": task.id})


@api_view(["GET"])
def report_status(request, report_id):
    report = get_object_or_404(UserReport, id=report_id)
    return Response(
        {
            "ready": bool(report.generated_at),
            "download_url": f"/api/reports/{report.id}/download/" if report.generated_at else None,
        }
    )


@api_view(["GET"])
def download_report(request, report_id):
    report = get_object_or_404(UserReport, id=report_id)
    if not report.file_path:
        raise Http404
    return FileResponse(open(settings.BASE_DIR / report.file_path, "rb"), as_attachment=True)


@api_view(["POST"])
def celery_fail_retry(request):
    task = failing_url_task.delay()
    return Response({"task_id": task.id})


@api_view(["POST"])
def classify_image(request):
    uploaded = UploadedImage.objects.create(image=request.FILES["image"])
    task = classify_uploaded_image.delay(uploaded.id)
    return Response({"image_id": uploaded.id, "task_id": task.id}, status=status.HTTP_201_CREATED)


@api_view(["POST"])
def celery_chain(request):
    task = chain(generate_random_number.s(), multiply_by_ten.s(), save_chain_result.s())()
    return Response({"task_id": task.id})


@api_view(["POST"])
def celery_priority_email(request):
    task = critical_email_task.apply_async(
        args=[request.data.get("email", "admin@example.com")],
        queue="priority_queue",
    )
    return Response({"task_id": task.id, "queue": "priority_queue"})


@api_view(["POST"])
def create_user_transaction(request):
    username = request.data.get("username", "transaction_user")

    with transaction.atomic():
        user = User.objects.create_user(username=username)
        transaction.on_commit(lambda: update_user_last_login.delay(user.id))

    return Response({"user_id": user.id})
