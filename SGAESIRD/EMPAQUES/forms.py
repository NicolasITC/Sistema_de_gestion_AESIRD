from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Usuario, Universidades, Turnos, Anuncios, Comentarios

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
class Turnos_form(forms.ModelForm):
    class Meta:
        model=Turnos
        fields={
            'hora_inicio',
            'hora_final',
            'fecha',
        }
    
class Editar_usuario_form(forms.ModelForm):
    class Meta:
        model = Usuario
        fields={
            'rut',
            'carrera',
            'telefono',
            'foto',
            'activo',
            'cant_turnos_disponibles',
        }
class Editar_usuario_form2(forms.ModelForm):
    class Meta:
        model = User
        fields={
            'username',
            'first_name',
            'last_name',
            'email',
        }

class AnunciosForm(forms.ModelForm):
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"inputText"})
    )
    contenido = forms.CharField(
        widget=forms.Textarea(attrs={'type':"text", 'class':"form-control", 'id':"inputText", 'rows':3})
    )
    class Meta:
        model = Anuncios
        fields = ("titulo","contenido",)

class ComentariosForm(forms.ModelForm):
    contenido = forms.CharField(
        widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"inputText", 'placeholder':"Escribe una respuesta..."})
    )
    class Meta:
        model = Comentarios
        fields = ("contenido",)