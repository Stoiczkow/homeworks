from django.db import models
from django.core.cache import cache


class Task(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        cache.delete("tasks")
        return super().save(*args, **kwargs)


class Place(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=300)
    body = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    
class LogEntry(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
class Website(models.Model):
    title = models.CharField(max_length=300)