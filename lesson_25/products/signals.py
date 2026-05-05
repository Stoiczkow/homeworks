from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.cache import cache

from .models import Product


@receiver(post_save, sender=Product)
def invalidate_product_cache_on_save(sender, instance, created, **kwargs):
    """
    Signal handler: Po każdym save produktu (update lub create),
    unieważnij cache dla szczegółów tego produktu i listy produktów.
    
    Parametry:
    - sender: Model Product
    - instance: Instancja produktu, która została zapisana
    - created: Boolean - True jeśli był to nowy obiekt, False jeśli update
    - **kwargs: Dodatkowe parametry
    """
    if not created:
        # Unieważnij cache dla szczegółów tego konkretnego produktu
        product_cache_key = f'product_retrieve_{instance.id}'
        cache.delete(product_cache_key)
        
        # Unieważnij cache dla listy produktów
        cache.delete('products_list')
