from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Task

@receiver(post_save, sender=Task)
def clear_task_cache_on_save(sender, instance, created, **kwargs):
    cache.clear()

@receiver(post_delete, sender=Task)
def clear_task_cache_on_delete(sender, instance, **kwargs):
    cache.clear()