from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView

from .models import Usuario

from .forms import SignUpForm, Usuario_Form



# Create your views here.
def home(request):
	return render(request, 'home.html', {})


def registrate(request):
    if request.method == "POST":
        form_account = SignUpForm(request.POST)
        form_usuario = Usuario_Form(request.POST)

        if form_account.is_valid() and form_usuario.is_valid():
            post_form_account = form_account.save(commit=False)
            post_form_usuario = form_usuario.save(commit=False)

            post_form_account.save()

            post_form_usuario.usuario = post_form_account
            post_form_usuario.rol = 'E'
            post_form_usuario.activo = 'A'
            post_form_usuario.cant_turnos_disponibles = 3

            post_form_usuario.save()
            

            return redirect('/')
    else:
        form_account = SignUpForm()
        form_usuario = Usuario_Form()


    return render(request, 'registration/registrate.html', {'form_account': form_account, 'form_usuario': form_usuario})

