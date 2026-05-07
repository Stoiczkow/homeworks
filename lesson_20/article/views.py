from django.shortcuts import render
from django.db import IntegrityError, connection
from django.http import HttpResponse
from .models import Article, Category
from datetime import date, timedelta

# Create your views here.
def create_article(request):
    new_title = request.GET.get('title')
    new_content = request.GET.get('content')
    category = request.GET.get('category')


    print(new_title)
    print(new_content)

    try:
        new_article = Article.objects.create(title=new_title,
                                            content = new_content,
                                            category_id=category)
    except IntegrityError:
        return HttpResponse("Artykuł nie mógł zostać stworzony na podstawie podanych danych")

    return HttpResponse(f"Stworzono artykuł {new_article.id}")

def filter_articles(request):

    # Przy parametrze wyszukiwania ignorujemy filtr wpisany przez użytkownika
    # Korzystam z icontains - wyczytałem że to do wyszukiwarki dobre, bo bierze pod uwagę wielkie i małe litery
    q_par = request.GET.get('q')
    if q_par:
        articles = Article.objects.filter(content__icontains=q_par)
    else:
    # Jeżeli nie ma parametru wyszukiwania, sprawdzamy filtr
        filter = request.GET.get('filter')
        articles = Article.objects.filter(id=filter)


    #articles = Article.objects.filter(title__="cos")

    # articles.title = "Zmieniony tytuł"
    # articles.save()

    return render(request, "article/article_list.html", {'articles': articles})

def view_categories(request):
    categories = Category.objects.all()

    return render(request, 'article/categories.html', {'categories': categories})

def category_detail_view(request, category_id):
    try: 
        object_category = Category.objects.get(id=category_id) 
        objects = object_category.article_set.all() 
        return render(request, "article/category_detail_view.html", {"object_category": object_category, "objects": objects}, ) 
    except Category.DoesNotExist: 
        return render(request, "404.html", {"messages": "Nie znaleziono rekorów o podanym ID"})