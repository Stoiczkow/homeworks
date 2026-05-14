from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Post


def home_view(request):
	query = request.GET.get('q', '').strip()
	posts = Post.objects.select_related('category').prefetch_related('tags').filter(
		is_published=True
	)

	if query:
		posts = posts.filter(
			Q(title__icontains=query) | Q(content__icontains=query)
		)

	posts = posts.order_by('-publication_date')[:5]

	return render(
		request,
		'home.html',
		{
			'categories': Category.objects.all(),
			'posts': posts,
			'query': query,
		},
	)


def category_posts_view(request, category_id):
	category = get_object_or_404(Category, pk=category_id)
	posts = Post.objects.select_related('category').prefetch_related('tags').filter(
		category=category
	).order_by('-publication_date')

	return render(
		request,
		'category_posts.html',
		{
			'category': category,
			'posts': posts,
		},
	)
