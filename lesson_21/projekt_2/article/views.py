from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category

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
    filter = request.GET.get('filter')

    articles = Article.objects.all()
#articles = Article.objects.filter(title__="Polsk")
# SELECT * FROM articles WHERE id=filter
    print(articles)

# articles.title = "Zmieniony tytuł"

# articles.save()


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