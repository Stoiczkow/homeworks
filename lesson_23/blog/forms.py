from django import forms

#task6
class SearchForm(forms.Form):
    text = forms.CharField(label="Tutaj wpisz szukany tekst",
                            max_length=200)