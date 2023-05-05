from django import forms
from .models import EmailSend


class EmailSendForm(forms.ModelForm):
    class Meta:
        model = EmailSend
        fields = ['email', 'subject', 'message']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'subject': forms.TextInput(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
        }
