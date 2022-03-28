from django import forms
from .models import *


class SendMailForm(forms.ModelForm):
    subject = forms.CharField(label = 'Theme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label = 'Content', widget=forms.Textarea(attrs={'class': 'form-control'}))
    name = forms.EmailField(label = 'E-mail', widget=forms.Textarea(attrs={'class': 'form-control'}))

    class Meta:
        model = SendMail
        fields = ['name', 'subject', 'content']