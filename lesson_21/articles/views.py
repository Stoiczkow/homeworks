from django.shortcuts import get_object_or_404, render

from .models import Article, Category


def article_list_view(request):
	query = request.GET.get('q', '').strip()
	articles = Article.objects.select_related('category').filter(is_published=True)

	if query:
		articles = articles.filter(title__icontains=query)

	return render(
		request,
		'article_list.html',
		{
			'articles': articles,
			'query': query,
		},
	)


def category_list_view(request):
	categories = Category.objects.all()
	return render(
		request,
		'categories.html',
		{
			'categories': categories,
		},
	)


def category_detail_view(request, pk):
	category = get_object_or_404(Category.objects.prefetch_related('articles'), pk=pk)
	return render(
		request,
		'category_detail.html',
		{
			'category': category,
		},
	)
