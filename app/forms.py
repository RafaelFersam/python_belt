from django import forms
from django.db.models import fields
from app.models import User


class UserForm(forms.ModelForm):
    
    password_confirm = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['name', 'email', 'password']
        labels = {
            'name': 'Nombre',
            'email': 'Email',
            'password': 'Contraseña',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        


class LoginForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email', 'password']
        labels = {
            'email': 'Email',
            'password': 'Contraseña',
        }
        
        widgets = {
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
