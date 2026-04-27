from django.contrib import admin

from .models import Article, Category
# Register your models here.

admin.site.register(Article)
admin.site.register(Category)
#task9
admin.site.site_header ="Panel Administratora Mojej Strony"