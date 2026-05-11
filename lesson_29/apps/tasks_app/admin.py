from django.contrib import admin

from apps.tasks_app.models import EmailNotification, LogEntry, ScrapedPage, UploadedImage


@admin.register(EmailNotification)
class EmailNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'recipient_email', 'subject', 'sent_at', 'created_at')
    list_filter = ('sent_at',)
    search_fields = ('recipient_email', 'subject')


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'created_at')
    list_filter = ('created_at',)


@admin.register(ScrapedPage)
class ScrapedPageAdmin(admin.ModelAdmin):
    list_display = ('id', 'url', 'title', 'scraped_at')


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'classification_result', 'uploaded_at')