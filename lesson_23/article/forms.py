from django import forms



#task10
class ArticleSearchForm(forms.Form):
    text = forms.CharField(label="Tutaj wpisz tekst: ", required=False)