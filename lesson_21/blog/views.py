from django.shortcuts import render, get_object_or_404

from .models import Category, Article


# Zadanie 3 – lista kategorii
def category_list_view(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories})


# Zadanie 6 – szczegóły kategorii (+ zadanie 7: lista artykułów)
def category_detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    return render(request, 'blog/category_detail.html', {'category': category})


# Zadanie 8 + 10 – lista artykułów (tylko opublikowane + wyszukiwanie)
def article_list_view(request):
    articles = Article.objects.filter(is_published=True)
    # Zadanie 10 – filtrowanie po tytule
    q = request.GET.get('q')
    if q:
        articles = articles.filter(title__icontains=q)
    return render(request, 'blog/article_list.html', {'articles': articles, 'q': q or ''})