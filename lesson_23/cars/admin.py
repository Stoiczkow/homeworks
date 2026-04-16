from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Dealer


class CarInline(admin.TabularInline):
    model = Car
    extra = 0


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    inlines = [CarInline]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'year', 'is_available', 'photo_preview')
    search_fields = ('brand', 'model')
    list_filter = ('is_available', 'year')
    ordering = ('-year',)
    
    def get_readonly_fields(self, request, obj=None):
        return ('year',) if obj else ()

    actions = ('mark_as_unavailable',)

    @admin.display(description='Pełna nazwa')
    def full_name(self, obj):
        return f"{obj.brand} {obj.model}"

    @admin.display(description='Zdjęcie')
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return " "

    @admin.action(description='Oznacz jako niedostępne')
    def mark_as_unavailable(self, request, queryset):
        updated = queryset.update(is_available=False)
        self.message_user(request, f'Oznaczono {updated} samochód(ów) jako niedostępne.')
