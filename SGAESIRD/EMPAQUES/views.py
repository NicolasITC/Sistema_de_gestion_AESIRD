from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone

from .models import Usuario, Turnos, Toma_turnos, Anuncios, Comentarios

from .forms import SignUpForm, Usuario_Form, Turnos_form, AnunciosForm, ComentariosForm
import datetime
from datetime import timedelta
import dateutil.parser

from django.core.mail import send_mail
from django.conf import settings


def turnos_base(actual, turnos):
    if(actual>=0):
        hoy=datetime.datetime.today()+ datetime.timedelta(weeks=actual)
    else:
        hoy=datetime.datetime.today()- datetime.timedelta(weeks=abs(actual))
        
    week=hoy.strftime("%Y-W%W") 
    start_week = datetime.datetime.strptime(week + '-1', "%Y-W%W-%w")
    end_week = start_week + datetime.timedelta(days=7)   
    start_week = dateutil.parser.parse(str(start_week)).date()
    end_week = dateutil.parser.parse(str(end_week)).date()
    turnos=turnos.filter(fecha__range=[start_week,end_week])
    return turnos

def get_semana(actual):
    if(actual>=0):
        hoy=datetime.datetime.today()+ datetime.timedelta(weeks=actual)
    else:
        hoy=datetime.datetime.today()- datetime.timedelta(weeks=abs(actual))
        
    week=hoy.strftime("%Y-W%W") 
    start_week = datetime.datetime.strptime(week + '-1', "%Y-W%W-%w")
    start_week = dateutil.parser.parse(str(start_week)).date()
    date_list = [start_week + datetime.timedelta(days=x) for x in range(7)]

    return date_list

@login_required
def home(request):
    now = datetime.datetime.today()
    if request.method == "POST":
        form_anuncio = AnunciosForm(request.POST)
        if form_anuncio.is_valid():
            post_form_anuncio = form_anuncio.save(commit=False)
            post_form_anuncio.usuario = Usuario.objects.filter(usuario = request.user)[:1].get()
            post_form_anuncio.save()
        anuncios=Anuncios.objects.all()
        retorno = ""
        registro = Toma_turnos.objects.filter(fecha_inicio__lte = now, fecha_termino__gte = now)
        if(len(registro)>0):
            retorno = "ahora"
    else:
        anuncios=Anuncios.objects.all()
        retorno = ""
        registro = Toma_turnos.objects.filter(fecha_inicio__lte = now, fecha_termino__gte = now)
        if(len(registro)>0):
            retorno = "ahora"
    
    informacion = Toma_turnos.objects.filter(fecha_termino__gte = now)
    form_anuncios = AnunciosForm()
    if(len(informacion)>0):
        return render(request, 'home.html', {'anuncios': anuncios, 'retorno':retorno, 'informacion':informacion[0], 'form_anuncios':AnunciosForm})
    else:
        return render(request, 'home.html', {'anuncios': anuncios, 'retorno':retorno, 'informacion':"no hay informacion", 'form_anuncios':AnunciosForm})

@login_required
def planilla_turnos(request, semana):
    turnos=Turnos.objects.all()
    start = datetime.datetime.strptime("07:00", "%H:%M")
    hora = [start + datetime.timedelta(minutes=x*30) for x in range(35)]
    sem=get_semana(semana)
    turnos = turnos_base(semana, turnos)
    return render(request, 'turnos.html', {'turnos':turnos, 'semana':semana,'sem':sem, 'hora':hora})
    
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
            post_form_usuario.fecha_ingreso = timezone.now()
            post_form_usuario.cant_turnos_disponibles = 3
            post_form_usuario.save()
            return redirect('registro_completado')
    else:
        form_account = SignUpForm()
        form_usuario = Usuario_Form()


    return render(request, 'registration/registrate.html', {'form_account': form_account, 'form_usuario': form_usuario})
    


@login_required
def toma_turnos(request, semana):
    turnos=Turnos.objects.all()
    start = datetime.datetime.strptime("07:00", "%H:%M")
    hora = [start + datetime.timedelta(minutes=x*30) for x in range(35)]
    sem=get_semana(semana)
    turnos = turnos_base(semana, turnos)

    return render(request, "toma_turnos.html",{'turnos':turnos, 'semana':semana,'sem':sem, 'hora':hora})

@login_required
def ver_anuncios(request, id_anun):
    anu=Anuncios.objects.filter(id_Anuncios=id_anun)
    if request.method == "POST":
        form_comentarios = ComentariosForm(request.POST)
        if form_comentarios.is_valid():
            post_form_comentarios = form_comentarios.save(commit=False)
            post_form_comentarios.usuario = Usuario.objects.filter(usuario = request.user)[:1].get()
            post_form_comentarios.anuncio = anu[:1].get()
            post_form_comentarios.save()

    form_comentarios = ComentariosForm
    com=Comentarios.objects.filter(anuncio__id_Anuncios=id_anun)
    if len(anu) > 0:
        if len(com) > 0:
            return render(request, "anuncios.html", {'anu':anu[0], 'com':com, 'form_comentarios':form_comentarios})
        else:
            return render(request, "anuncios.html", {'anu':anu[0], 'com':None, 'form_comentarios':form_comentarios})    
    else:
        return render(request, "anuncios.html", {'anu':None, 'com':None, 'form_comentarios':form_comentarios})



def registro_completado(request):
    return render(request,"registration/registro_completado.html")


def asignar_turnos(request):
    semana=1
    turnos=Turnos.objects.all()
    start = datetime.datetime.strptime("07:00", "%H:%M")
    hora = [start + datetime.timedelta(minutes=x*30) for x in range(35)]
    sem=get_semana(semana)
    turnos = turnos_base(semana, turnos)
    return render(request, 'asignar_turnos.html', {'turnos':turnos, 'semana':semana,'sem':sem, 'hora':hora})