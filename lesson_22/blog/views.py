from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from .models import Post, Category


# Zadanie 3 (rozbudowane w zad. 6) – strona główna
class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        # Zadanie 3 – 5 najnowszych postów (order_by + slicing)
        queryset = Post.objects.order_by('-published_at')

        # Zadanie 6 – wyszukiwarka: filtruj gdy podana fraza
        q = self.request.GET.get('q', '').strip()
        if q:
            queryset = (
                Post.objects.filter(title__icontains=q) |
                Post.objects.filter(content__icontains=q)
            ).order_by('-published_at')
            return queryset

        return queryset[:5]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q', '')
        return context


# Zadanie 2 – lista postów danej kategorii (filter() na QuerySet)
class CategoryPostListView(ListView):
    model = Post
    template_name = 'blog/category_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, pk=self.kwargs['category_id'])
        # Zadanie 2 – użycie filter()
        return Post.objects.filter(category=self.category).order_by('-published_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        return context
