from django.contrib import admin

from .models import Category, Note, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('id', 'name')
	search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'price', 'category')
	list_filter = ('category',)
	search_fields = ('name', 'description')


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
	list_display = ('id', 'title')
	search_fields = ('title', 'content')

# Register your models here.
