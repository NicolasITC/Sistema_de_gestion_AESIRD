from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


from .models import Usuario, Universidades, Turno, Anuncios, Comentarios, Lista_de_Espera, Anotaciones, Toma_turnos, Mensaje_inicio, Categoria_anotaciones

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
            'universidad',
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

class Agregar_Lista_Espera(forms.ModelForm):
    class Meta:
        model=Lista_de_Espera
        fields={
            'rut',
            'nombre',
            'apellido',
            'carrera',
            'universidad',
            'telefono',
        }
class AnotacionesForm(forms.ModelForm):
    class Meta:
        model=Anotaciones
        fields={
            'categoria_anotaciones',
            'turnos_restados',
        }
class TomaturnosForm(forms.Form):
    fecha_inicio = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )
    lugar_reunion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"inputText", 'placeholder':"Escribe una respuesta..."}))
class Mensaje_inicioForm(forms.ModelForm):
    titulo = forms.CharField(
        widget=forms.TextInput(attrs={'type':"text", 'class':"form-control", 'id':"inputText"})
    )
    mensaje = forms.CharField(
        widget=forms.Textarea(attrs={'type':"text", 'class':"form-control", 'id':"inputText", 'rows':3})
    )

    class Meta:
        model = Mensaje_inicio
        fields = ("titulo","mensaje",)

class TurnoForm(forms.ModelForm):
    class Meta:
        model = Turno
        fields = ("emp01","emp02","emp03","emp04","emp05","emp06","emp07","emp08","emp09","emp10","emp11","emp12","emp13",)

class Categoria_anotacionesForm(forms.ModelForm):
    class Meta:
        model = Categoria_anotaciones
        fields = ("nombre_anotacion",)