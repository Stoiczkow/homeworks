from django.contrib import admin

from .models import EmailNotification, LogEntry


@admin.register(EmailNotification)
class EmailNotificationAdmin(admin.ModelAdmin):
    list_display = ("id", "recipient_email", "subject", "sent_at")
    search_fields = ("recipient_email", "subject")
    list_filter = ("sent_at",)

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ("id", "message", "created_at")
    search_fields = ("message",)
    list_filter = ("created_at",)