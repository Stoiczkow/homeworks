from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category
from datetime import timedelta
from django.utils import timezone

def create_article(request):
    new_title = request.GET.get('title')
    new_content = request.GET.get('content')

    print(new_title)
    print(new_content)

    new_article = Article.objects.create(
    title=new_title,
    content=new_content
    )

    return HttpResponse(f"Stworzono artykuł: {new_article.id}")

def filter_articles(request):
    # Pobieranie parametru q z get
    search_query = request.GET.get('q', '')
    
    # Filtrowanie artykułów po tytule zawierającym szukaną frazę
    if search_query:
        articles = Article.objects.filter(
            is_published=True,
            title__icontains=search_query
        )
    else:
        articles = Article.objects.filter(is_published=True)
    
    # Obliczanie która data była 3 dni temu
    three_days_ago = timezone.now() - timedelta(days=3)
    
    # Dodanie is_new dla artykułów z ostatnich 3 dni
    for article in articles:
        article.is_new = article.pub_date >= three_days_ago

    return render(request, "article/article_list.html", {'articles': articles})

def  view_categories(request): # Zaimportowany z category.py
    categories = Category.objects.all() # all wszystkie rektody pobierze 

    return render(request, "article/categories.html", {"categories": categories})
# pobiera wszystkie kategorie

def category_detail_view(request, category_id):
    try:
        selcted_category = Category.objects.get(id=category_id)
    
    except Category.DoesNotExist:
        selcted_category = None

    return render(request,"article/category_detail_view.html", {"category": selcted_category})