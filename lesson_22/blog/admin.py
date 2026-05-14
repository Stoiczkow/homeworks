from django.contrib import admin

from .models import Category, Post, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'category', 'publication_date', 'is_published')
	list_filter = ('category', 'is_published', 'tags')
	search_fields = ('title', 'content')
	filter_horizontal = ('tags',)
