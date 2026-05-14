from django.db import models
from django.utils import timezone


class EmailNotification(models.Model):
	recipient_email = models.EmailField()
	subject = models.CharField(max_length=200)
	body = models.TextField()
	sent_at = models.DateTimeField(blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'{self.recipient_email} - {self.subject}'


class LogEntry(models.Model):
	message = models.CharField(max_length=255)
	created_at = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'{self.created_at:%Y-%m-%d %H:%M:%S} - {self.message}'


class ScrapedPageTitle(models.Model):
	url = models.URLField(default='https://example.com')
	title = models.CharField(max_length=255)
	fetched_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-fetched_at']

	def __str__(self):
		return self.title


class GeneratedCsvReport(models.Model):
	task_id = models.CharField(max_length=100, unique=True, blank=True)
	report_file = models.FileField(upload_to='reports/', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	completed_at = models.DateTimeField(blank=True, null=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'Raport {self.pk}'


class UploadedImage(models.Model):
	image = models.ImageField(upload_to='uploaded_images/')
	classification_result = models.CharField(max_length=255, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ['-created_at']

	def __str__(self):
		return f'Obraz {self.pk}'
