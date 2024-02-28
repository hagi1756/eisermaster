# from django.forms import ModelForm
# from core.models import Contact
# from django import forms

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields =['name','email','subject','message']


#         widgets = {

#                    'name': forms.TextInput(attrs={'placeholder':'Name'}),
#                    'email': forms.EmailInput(attrs={'placeholder':'Email'}),
#                    'message': forms.Textarea(attrs={'placeholder':'Message'}),
#                    'subject': forms.TextInput(attrs={'placeholder':'Subject'})
#                    }



# from django.forms import ModelForm
# from core.models import Contact
# from django import forms

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'subject', 'message']

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message', 'rows': 4}),
#             'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'})
#         }



# from django.forms import ModelForm
# from core.models import Contact
# from django import forms

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'email', 'subject', 'message']

#         widgets = {
#             'name': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Name', 'style': 'background-color: #f8f9fa;'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Email', 'style': 'background-color: #f8f9fa;'}),
#             'message': forms.Textarea(attrs={'class': 'form-control rounded-0', 'placeholder': 'Message', 'rows': 4, 'style': 'background-color: #f8f9fa;'}),
#             'subject': forms.TextInput(attrs={'class': 'form-control rounded-0', 'placeholder': 'Subject', 'style': 'background-color: #f8f9fa;'}),
#         }



from django.forms import ModelForm
from core.models import Contact
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


