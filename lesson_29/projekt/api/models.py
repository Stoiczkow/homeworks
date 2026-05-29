from django.db import models
from django.utils import timezone


# Zadanie 10 – model powiadomienia email
class EmailNotification(models.Model):
    recipient_email = models.EmailField()
    subject = models.CharField(max_length=200)
    body = models.TextField()
    sent_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.subject} → {self.recipient_email}"


# Zadanie 12 – model wpisu logu do czyszczenia
class LogEntry(models.Model):
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"[{self.created_at:%Y-%m-%d %H:%M}] {self.message[:60]}"


# Zadanie 13 – model scraped tytułu strony
class ScrapedTitle(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=500)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.url} – {self.title}"


# Zadanie 16 – model przesłanego obrazu z klasyfikacją
class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    classification_result = models.CharField(max_length=500, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.pk}: {self.classification_result or 'nie sklasyfikowano'}"
