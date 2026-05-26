from django.shortcuts import render, get_object_or_404
from .models import Article, Category, Author


def home(request):
    articles = Article.objects.order_by('-published_date')[:5]
    return render(request, 'app_Article/home.html', {'articles': articles})


def search(request):
    query = request.GET.get('q', '')
    articles = Article.objects.filter(
        title__icontains=query
    ) | Article.objects.filter(
        content__icontains=query
    )
    return render(request, 'app_Article/search.html', {
        'query': query,
        'articles': articles,
    })


def articles_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    articles = Article.objects.filter(category_id=category_id)
    return render(request, 'app_Article/category_articles.html', {
        'category': category,
        'articles': articles,
    })


def articles_by_author(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    articles = Article.objects.filter(author_id=author_id)
    return render(request, 'app_Article/author_articles.html', {
        'author': author,
        'articles': articles,
    })
