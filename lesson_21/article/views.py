from django.shortcuts import render
from django.http import HttpResponse
from .models import Article, Category

from .models import Article

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
    # articles = Article.objects.filter(id=filter)
    # articles = Article.objects.filter(title__contains="Polska")
    # SELECT * FROM articles WHERE id=filter
    print(articles)

    # articles.title = "Zmieniony tytuł"

    # articles.save()

    # if articles:
    return render(request, "article/article_list.html", {'articles': articles})

    # return HttpResponse("Nie znaleziono rekordów")

def view_categories(request):
    categories = Category.objects.all()

    return render(request, 'article/categories.html', {'categories': categories})


def category_detail_view(request, category_id):
    try:
        selected_category = Category.objects.get(id=category_id)

    except Category.DoesNotExist:
        selected_category = None

    return render(request, 'article/category_detail_view.html', {'category': selected_category})


def category_detail(request, cat_id):
    try:

        category = Category.objects.get(id=cat_id)
        articles = category.article_set.all()
    except Category.DoesNotExist:
        category = None
        articles = None

    return render(request, 'article/category_detail.html', {'category': category, 'articles': articles})

