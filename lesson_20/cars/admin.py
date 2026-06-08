from django.contrib import admin, messages
from .models import Car, Dealer
from django.utils.html import format_html

# Register your models here.

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):

    list_display = ['display_photo', 'brand', 'model', 'year', 'is_available', 'full_name']
    search_fields = ['brand, model']
    list_filter = ['is_available', 'year']
    ordering = ['-year']
    readonly_fields = ['year']
    actions = ['mark_as_unavailable']

    def full_name(self, obj):
        return f"{obj.brand} - {obj.model}"
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('year',)
        return ()
    
    full_name.short_description = "Pełna nazwa"

    def display_photo(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        else:
            return "Brak zdjęcia"
        
    def mark_as_unavailable(self, request, queryset):
        rows_updated = queryset.update(is_available=False)
        self.message_user(request, f'{rows_updated} samochodów oznaczonych jako niedostępne', messages.SUCCESS)
    
    mark_as_unavailable.short_description = "Oznacz samochód jako niedostępny"


class CarInLine(admin.TabularInline):
    model = Car
    extra = 1

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    inlines = [CarInLine]
