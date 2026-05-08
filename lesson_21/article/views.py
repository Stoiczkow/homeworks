from datetime import timedelta

from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Article, Category


def category_list_view(request):
    categories = Category.objects.order_by('name')
    return render(request, 'article/category_list.html', {'categories': categories})


def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    articles = category.article_set.filter(is_published=True).order_by('-pub_date')
    return render(
        request,
        'article/category_detail.html',
        {'category': category, 'articles': articles},
    )


def article_list_view(request):
    query = request.GET.get('q', '')
    articles = Article.objects.filter(is_published=True).order_by('-pub_date')

    if query:
        articles = articles.filter(title__icontains=query)

    recent_limit = timezone.now() - timedelta(days=3)
    return render(
        request,
        'article/article_list.html',
        {
            'articles': articles,
            'query': query,
            'recent_limit': recent_limit,
        },
    )
