from django.contrib import admin
from django.utils.html import format_html
from .models import Car, Dealer


# zadanie 8 - akcja niestandardowa
@admin.action(description='Oznacz jako niedostepne')
def mark_as_unavailable(modeladmin, request, queryset):
    updated = queryset.update(is_available=False)
    modeladmin.message_user(request, f'Oznaczono {updated} samochod(ow) jako niedostepne.')


# zadanie 10 - Inline dla Dealera
class CarInline(admin.TabularInline):
    model = Car
    extra = 1


# zadania 2-9 - pełna konfiguracja CarAdmin
@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # zadanie 2 - kolumny
    list_display = ('make', 'model', 'year', 'is_available', 'full_name', 'photo_preview')

    # zadanie 3 - wyszukiwanie
    search_fields = ('make', 'model')

    # zadanie 4 - filtry
    list_filter = ('is_available', 'year')

    # zadanie 5 - sortowanie
    ordering = ('-year',)

    # zadanie 7 - pole tylko do odczytu
    readonly_fields = ('year',)

    # zadanie 8 - akcja
    actions = [mark_as_unavailable]

    # zadanie 6 - pole dynamiczne "Pelna nazwa"
    @admin.display(description='Pelna nazwa')
    def full_name(self, obj):
        return f"{obj.make} {obj.model}"

    # zadanie 9 - miniaturka zdjecia
    @admin.display(description='Zdjecie')
    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" />', obj.photo.url)
        return '-'


# zadanie 10 - Dealer z Inline
@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    inlines = [CarInline]
