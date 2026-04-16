from django import forms

class SearchForm(forms.Form):
    phrase = forms.CharField(
        label='Szukana fraza',
        max_length=100
    )