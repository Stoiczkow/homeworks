from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Nazwa produktu', max_length=20)
    desc = forms.CharField(label='Opis produktu', widget=forms.Textarea)
    price = forms.FloatField(label="Cena")