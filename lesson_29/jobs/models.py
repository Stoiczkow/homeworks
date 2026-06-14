from django.db import models

from django.utils import timezone


class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject} -> {self.recipient_email}"
    
class LogEntry(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.message[:50]} - {self.created_at}"