from django import forms


class SendMailForm(forms.ModelForm):
    subject = forms.CharField(label = 'Theme', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label = 'Content', widget=forms.Textarea(attrs={'class': 'form-control'}))

