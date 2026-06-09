from django.contrib import admin

from .models import Reservation, Screening
# Register your models here.

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['user', 'screening', 'number_of_places', 'status', 'creat_at']

@admin.register(Screening)
class ScreeningAdmin(admin.ModelAdmin):
    # list_display = ['movie']
    pass