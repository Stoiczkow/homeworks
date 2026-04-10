from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from datetime import timedelta

from .models import Article, Category
from .forms import SearchForm

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
    articles = Article.objects.filter(is_published=True)

    form = SearchForm(request.GET or None)

    if form.is_valid():
        q = request.GET.get('q')

        if q:
            articles = articles.filter(title__icontains=q)

    for article in articles:
        article.is_new = article.pub_date >= timezone.now() - timedelta(days=3)

    return render(request, "article/article_list.html", {
        'articles': articles,
        'form': form
    })

def category_view(request):
    all_categories = Category.objects.all()
    
    return render(request, "article/categories.html", {'categories': all_categories})
    
def category_detail_view(request, category_id):
    try:
        category = Category.objects.get(id=category_id)
        articles = category.article_set.filter(is_published=True)
    except Category.DoesNotExist:
        print("Nie ma kategorii z takim id") 
        category = ''
    return render(request, "article/category_detail.html", 
                  {
                      'category': category,
                      'articles': articles
                      })