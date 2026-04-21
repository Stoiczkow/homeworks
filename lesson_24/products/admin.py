from django.contrib import admin

from .models import Product3


@admin.register(Product3)
class ProductAdmin(admin.ModelAdmin):
    pass