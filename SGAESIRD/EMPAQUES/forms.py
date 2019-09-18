from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Usuario, Universidades

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=140, required=True)
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

class Usuario_Form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = {
            'rut',
            'carrera',
            'universidad',
            'telefono',
            
        }
    