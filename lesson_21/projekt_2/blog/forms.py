from django import forms

class SeargeForm(forms.Form):
    phrase = forms.CharField(max_length=100)