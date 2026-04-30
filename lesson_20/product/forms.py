from django import forms
from .models import Product

#task7
class ProductForm(forms.Form):
    name = forms.CharField(label='nazwa produktu:' ,max_length=100)
    description = forms.CharField(label='opis:' ,widget=forms.Textarea)
    price = forms.DecimalField(label='cena:' ,max_digits=6, decimal_places=2)
