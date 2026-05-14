from django import forms
from django.contrib.auth.models import User

from .models import EmailNotification, UploadedImage


class MultiplyForm(forms.Form):
    a = forms.IntegerField(label='Liczba A')
    b = forms.IntegerField(label='Liczba B')


class UpdateLastLoginForm(forms.Form):
    user = forms.ModelChoiceField(label='Użytkownik', queryset=User.objects.order_by('username'))


class EmailNotificationForm(forms.ModelForm):
    class Meta:
        model = EmailNotification
        fields = ['recipient_email', 'subject', 'body']
        widgets = {'body': forms.Textarea(attrs={'rows': 4})}


class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']