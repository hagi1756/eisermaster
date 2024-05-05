



from django.forms import ModelForm
from core.models import Contact,Subscriber
from django import forms

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'style': 'background-color: #ffeeba; color: #dc3545;'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'style': 'background-color: #ffe8f1; color: #6610f2;'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 4, 'style': 'background-color: #d4edda; color: #28a745;'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject', 'style': 'background-color: #cdeefd; color: #007bff;'}),
        }


class SubscriberForm(ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={'placeholder':'Your Email Address', 'class':'form-control'}),
        }

 