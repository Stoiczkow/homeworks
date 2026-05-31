from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from .models import Product, Note, Author, Book, EmailNotification, LogEntry
from .serializer import ProductSerializer, NoteSerializer, AuthorSerializator, BookSerializator



from datetime import timedelta
from django.db.models.functions import Now

from .tasks import (simulate_cpu_bound_task, 
                    hello_world,multiply, 
                    log_timestamp, 
                    count_user, 
                    update_user_last_login,
                    video_processing_simulation,
                    task_EmailNotification,
                    clear_log_Entry
                    )
from django.http import HttpResponse

# class ProductViewSet(viewsets.ModelViewSet):
#     querysets = Product.objects.all()
#     serializer_class = ProductSerializer



class ProductViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        
        min_price = self.request.query_params.get('min_price')
        max_price = self.request.query_params.get('max_price')

        if min_price is not None:
            queryset = queryset.filter(price__gte=min_price)
            
        if max_price is not None:
            queryset = queryset.filter(price__lte=max_price)

        return queryset


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer



# class ProductViewSet(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer




@api_view(['GET'])
def setName(request):

    response = Response({"message" : "Ustawiono ciasteczko"})

    name = request.GET.get('name')

    response.set_cookie('username', name, max_age=3600 )

    return response


@api_view(['GET'])
def helloview(request):

    username = request.COOKIES.get("username", 'Bezimienny')

    return Response({"message" : f"Witaj, {username}!"})



class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializator



class BookViewSet(viewsets.ModelViewSet):

    queryset = Book.objects.all()
    serializer_class = BookSerializator


@api_view(['GET'])
def test_celery(request):
    task = simulate_cpu_bound_task.delay(20)
    return Response({"message" : "Zadanie jest w trakcie wykonywania", 
                    "task_id" : task.id})
#task1
@api_view(["GET"])
def test_hello_world(request):
    hello_world.delay()
    return Response({"message": "Zadanie wysłane do Celery!"})


#task2
@api_view(["GET"])
def test_multiply(request):
    a = request.query_params.get("a")
    b = request.query_params.get('b')

    multiply.delay(float(a),float(b))
    return Response({"message": "wykonano obliczenie"})

#task3
@api_view(["GET"])
def test_time(request):

    log_timestamp.delay()
    return Response({"message": "Aktualny czas"})


#task 5
@api_view(["GET"])
def test_count_user(request):
    count_user.delay()
    return Response({"message" : "Lista uzytkownikow"})

#task 7
@api_view(["GET"])
def test_update_user_last_login(request):
    user_id = request.query_params.get('user_id')
    update_user_last_login.delay(user_id)
    return Response({"message" : "zaktualizowano pole last login"})

#task8
@api_view(["GET"])
def test_video_processing_simulation(request):
    video_processing_simulation.delay()

    return Response({"message" : "Przetwarzanie wideo rozpoczęte!"})

#task10
@api_view(["POST"])
def test_EmailNotification(request):
    
    if request.method == 'POST':
    
        recipient = request.data.get('email_address')
        subj = request.data.get('subject_text')
        content = request.data.get('message_body')

        
        new_email = EmailNotification.objects.create(
            recipient_email=recipient,
            subject=subj,
            body=content
        )
        task_EmailNotification.delay(new_email.id)

        return Response({"message" : "Stworzono maila i dodano doCelery"})



#task12
@api_view(["GET"])
def test_log_Entry(request):
    

    clear_log_Entry.delay()
    return Response({'message' : 'Zaczeto usuwac logi'})





























 
    