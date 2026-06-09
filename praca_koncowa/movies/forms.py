from django import forms

class SearchMoviesForm(forms.Form):
    name = forms.CharField(max_length=200, required=False,widget=forms.TextInput(attrs={
            'placeholder': 'Szukaj...',
            'class': 'search-input'  # dodal to chat aby odwolywac sie dotego w html
        }))

    def __str__(self):
        return self.name