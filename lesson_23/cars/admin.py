from django.contrib import admin, messages
from django.utils.html import format_html

from .models import Car, Dealer


class CarInline(admin.TabularInline):
	model = Car
	extra = 0
	fields = ('brand', 'model', 'year', 'price', 'is_available')


@admin.action(description='Oznacz jako niedostępne')
def mark_as_unavailable(modeladmin, request, queryset):
	updated = queryset.update(is_available=False)
	modeladmin.message_user(
		request,
		f'Oznaczono {updated} samochodów jako niedostępne.',
		level=messages.SUCCESS,
	)


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
	list_display = (
		'thumbnail',
		'full_name',
		'brand',
		'model',
		'year',
		'is_available',
	)
	search_fields = ('brand', 'model')
	list_filter = ('is_available', 'year')
	ordering = ('-year',)
	readonly_fields = ('year',)
	actions = (mark_as_unavailable,)

	@admin.display(description='Pełna nazwa')
	def full_name(self, obj):
		return f'{obj.brand} {obj.model}'

	@admin.display(description='Miniaturka')
	def thumbnail(self, obj):
		if not obj.photo:
			return 'Brak zdjęcia'
		return format_html('<img src="{}" width="150" alt="{}">', obj.photo.url, self.full_name(obj))


@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
	list_display = ('name', 'address')
	search_fields = ('name', 'address')
	inlines = [CarInline]
