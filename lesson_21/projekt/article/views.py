from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Article, Category


def create_article(request):
    new_title = request.GET.get('title')
    new_content = request.GET.get('content')
    new_article = Article.objects.create(title=new_title, content=new_content)
    return HttpResponse(
        f'Stworzono obiekt o tytule {new_title} i contencie: {new_content}, nowe id: {new_article.id}'
    )


def filter_article(request):
    new_filter = request.GET.get('filter')
    articles = Article.objects.filter(title__contains=new_filter)
    return render(request, 'article_list.html', {'articles': articles})


def article_list_view(request):
    articles = Article.objects.filter(is_published=True)
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    three_days_ago = timezone.now() - timezone.timedelta(days=3)
    return render(request, 'article_list.html', {
        'articles': articles,
        'three_days_ago': three_days_ago,
        'q': q or '',
    })


def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'categories.html', {'categories': categories})


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'category_detail.html', {'category': category})
