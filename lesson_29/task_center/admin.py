from django.contrib import admin

from .models import EmailNotification, GeneratedCsvReport, LogEntry, ScrapedPageTitle, UploadedImage


@admin.register(EmailNotification)
class EmailNotificationAdmin(admin.ModelAdmin):
	list_display = ['recipient_email', 'subject', 'created_at', 'sent_at', 'is_sent']
	search_fields = ['recipient_email', 'subject', 'body']
	list_filter = ['created_at', 'sent_at']

	@admin.display(boolean=True, description='Wysłane')
	def is_sent(self, obj):
		return obj.sent_at is not None


@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['short_message', 'created_at']
	search_fields = ['message']
	list_filter = ['created_at']

	@admin.display(description='Treść')
	def short_message(self, obj):
		return obj.message[:80]


@admin.register(ScrapedPageTitle)
class ScrapedPageTitleAdmin(admin.ModelAdmin):
	list_display = ['url', 'title', 'fetched_at']
	search_fields = ['url', 'title']
	list_filter = ['fetched_at']


@admin.register(GeneratedCsvReport)
class GeneratedCsvReportAdmin(admin.ModelAdmin):
	list_display = ['id', 'task_id', 'created_at', 'completed_at', 'file_ready']
	search_fields = ['task_id']
	list_filter = ['created_at', 'completed_at']
	readonly_fields = ['task_id', 'created_at', 'completed_at']

	@admin.display(boolean=True, description='Plik gotowy')
	def file_ready(self, obj):
		return bool(obj.report_file)


@admin.register(UploadedImage)
class UploadedImageAdmin(admin.ModelAdmin):
	list_display = ['id', 'created_at', 'classification_result_short']
	search_fields = ['classification_result']
	list_filter = ['created_at']
	readonly_fields = ['classification_result', 'created_at']

	@admin.display(description='Klasyfikacja')
	def classification_result_short(self, obj):
		return obj.classification_result[:80] or 'Brak'
