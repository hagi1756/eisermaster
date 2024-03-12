from django import forms
from .models import Myuser


class RegisterForm(forms.ModelForm):
    class Meta:
        model = Myuser
        fields = ['username','first_name','last_name','email','password','phone','country','city','date_of_birth','profile_pic']
        widgets = {
            'password': forms.PasswordInput(),
            'date_of_birth': forms.DateInput(attrs={'type': 'date','class':'form-control'}),
            'profile_pic': forms.FileInput(attrs={'class':'form-control'}),
        }


    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print('confirm_password',confirm_password)
        if password != confirm_password:
            raise forms.ValidationError("confirm_password", "Passwords don't match")
        return cleaned_data
    


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput( ))
    password = forms.CharField(widget=forms.PasswordInput())