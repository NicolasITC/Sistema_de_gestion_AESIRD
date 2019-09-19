from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Usuario, Turnos

from .forms import SignUpForm, Usuario_Form
import datetime


@login_required
def home(request):
    return render(request, 'home.html', {})


@login_required
def planilla_turnos(request, semana):
    turnos=Turnos.objects.all()
    start = datetime.datetime.strptime("07:00", "%H:%M")
    hora = [start + datetime.timedelta(minutes=x*30) for x in range(35)]
    return render(request, 'turnos.html', {'turnos':turnos, 'semana':semana, 'hora':hora})
    
@login_required
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
            post_form_usuario.fecha_ingreso = timezone.now
            post_form_usuario.cant_turnos_disponibles = 3
            post_form_usuario.save()
            return redirect('/')
    else:
        form_account = SignUpForm()
        form_usuario = Usuario_Form()


    return render(request, 'registration/registrate.html', {'form_account': form_account, 'form_usuario': form_usuario})

