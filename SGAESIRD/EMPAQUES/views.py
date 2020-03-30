from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Usuario, Turnos, Toma_turnos, Anuncios, Comentarios, User, Lista_de_Espera, Anotaciones, Mensaje_inicio

from .forms import SignUpForm, Usuario_Form, Turnos_form, Editar_usuario_form, Editar_usuario_form2, Agregar_Lista_Espera, TomaturnosForm, Mensaje_inicioForm, AnunciosForm, ComentariosForm, AnotacionesForm

import datetime
from datetime import timedelta
import dateutil.parser

from django.core.mail import send_mail
from django.conf import settings

now = datetime.datetime.today()
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
    
    if request.method == "POST":
        form_anuncio = AnunciosForm(request.POST)
        if form_anuncio.is_valid():
            post_form_anuncio = form_anuncio.save(commit=False)
            post_form_anuncio.usuario = Usuario.objects.filter(usuario = request.user)[:1].get()
            post_form_anuncio.save()
        anuncios=Anuncios.objects.all()
        retorno = ""
        registro = Toma_turnos.objects.filter(fecha_inicio__lte = now)
        if(len(registro)>0):
            retorno = "ahora"
    else:
        anuncios=Anuncios.objects.all()
        retorno = ""
        registro = Toma_turnos.objects.filter(fecha_inicio__lte = now)
        if(len(registro)>0):
            retorno = "ahora"
    mensajeinicio= Mensaje_inicio.objects.latest('fecha')
    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    if(len(informacion)==0):
        info = "no hay informacion"
    else:
        info = informacion[0]

    form_anuncios = AnunciosForm()
    return render(request, 'home.html', {'anuncios': anuncios, 'retorno':retorno, 'informacion':info, 'form_anuncios':AnunciosForm, 'mensaje_inicio':mensajeinicio})

def lista(request):
    listas=Lista_de_Espera.objects.all()
    retorno = ""
    now = datetime.datetime.today()
    registro = Toma_turnos.objects.filter(fecha_inicio__lte = now, fecha_inicio__gte = now)
    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    if(len(registro)>0):
        retorno = "ahora"
    print(len(informacion))
    if(len(informacion)>0):
        return render(request, 'lista_espera.html', {'listas': listas, 'retorno':retorno, 'informacion':informacion[0]})
    else:
        return render(request, 'lista_espera.html', {'listas': listas, 'retorno':retorno, 'informacion':"no hay informacion"})

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

    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    if(len(informacion)==0):
        info = "no hay informacion"
    else:
        info = informacion[0]

    if len(anu) > 0:
        if len(com) > 0:
            return render(request, "anuncios.html", {'anu':anu[0], 'com':com, 'informacion':info, 'form_comentarios':form_comentarios})
        else:
            return render(request, "anuncios.html", {'anu':anu[0], 'com':None, 'informacion':info, 'form_comentarios':form_comentarios})    
    else:
        return render(request, "anuncios.html", {'anu':None, 'com':None, 'informacion':info, 'form_comentarios':form_comentarios})


@login_required
def registro_completado(request):
    return render(request,"registration/registro_completado.html")

@login_required
def asignar_turnos(request):
    semana=1
    turnos=Turnos.objects.all()
    start = datetime.datetime.strptime("07:00", "%H:%M")
    hora = [start + datetime.timedelta(minutes=x*30) for x in range(35)]
    sem=get_semana(semana)
    turnos = turnos_base(semana, turnos)
    return render(request, 'asignar_turnos.html', {'turnos':turnos, 'semana':semana,'sem':sem, 'hora':hora})

@login_required
def finanzas(request):
    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    if(len(informacion)==0):
        info = "no hay informacion"
    else:
        info = informacion[0]
    return render(request,"finanzas.html", {'informacion':info})

def ver_perfil(request, id_perfil):
    perfil=Usuario.objects.filter(id_Usuario=id_perfil)
    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    if(len(informacion)==0):
        info = "no hay informacion"
    else:
        info = informacion[0]
    anotaciones=Anotaciones.objects.filter(usuario__id_Usuario=id_perfil)
    turnos=Turnos.objects.filter(usuario__id_Usuario=id_perfil)
    current_user = request.user
    if len(anotaciones) > 0:
        a=anotaciones
    else:
        a=None
    if len(turnos) > 0:
        b=turnos
    else:
        b=None    
    return render(request, 'perfil.html', {'perfil':perfil, 'id_perfil':id_perfil, 'anotaciones':a, 'informacion':info, 'turnos':b, 'current_user':current_user.id})    
       

def editar_perfil(request, pk):
    post2 = get_object_or_404(User, pk=pk)
    post = get_object_or_404(Usuario, pk=pk)
    if request.method == "POST":
        form2 = Editar_usuario_form2(request.POST, instance=post2)
        form = Editar_usuario_form(request.POST, request.FILES, instance=post)
        if form.is_valid() and  form2.is_valid:
            post = form.save(commit=False)
            post2 = form2.save(commit=False)
            post.save()
            post2.save()
            return redirect('ver_perfil', id_perfil=pk)
    else:
        form = Editar_usuario_form(instance=post)
        form2 = Editar_usuario_form2(instance=post2)
    
    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    if(len(informacion)==0):
        info = "no hay informacion"
    else:
        info = informacion[0]

    return render(request, 'form_editar_perfil.html', {'form2': form2, 'form': form, 'informacion':info, 'pk':pk})


def agregar_lista(request):
    if request.method == "POST":
        form=Agregar_Lista_Espera(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.fecha_ingreso = timezone.now()
            post.save()
            return redirect('listar')
    else:
        form=Agregar_Lista_Espera()
    
    return render(request,'agregar_lista_espera.html',{'form':form})

@login_required
def administracion(request):
    Lista_empaques = Usuario.objects.all()
    if request.method == "POST":
        form = TomaturnosForm(request.POST)
        form_mensaje = Mensaje_inicioForm(request.POST)
        if form.is_valid():
            post = form.save(commit=True)
            post.save()
       
        if form_mensaje.is_valid():
            post2 = form_mensaje.save(commit=True)
            post2.save() 
    else:
        form_mensaje = Mensaje_inicioForm()
        form = TomaturnosForm()


    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)

    return render(request,"administracion.html", {'informacion':informacion, 'lista_empaques':Lista_empaques, 'TomaturnosForm':TomaturnosForm, 'form_mensaje':form_mensaje})

@login_required
def ingresar_anotacion(request, pk):
    perfil=Usuario.objects.filter(id_Usuario=pk)
    anotaciiones=Anotaciones.objects.filter(usuario__id_Usuario=pk)

    if request.method == "POST":
        form_anotaciones = AnotacionesForm(request.POST)
        if form_anotaciones.is_valid():
            post_form_anotaciones = form_anotaciones.save(commit=False)
            post_form_anotaciones.usuario = Usuario.objects.filter(id_Usuario = pk)[:1].get()
            post_form_anotaciones.save()

    form_anotaciones = AnotacionesForm

    informacion = Toma_turnos.objects.filter(fecha_inicio__gte = now)
    
    if(request.user.usuario.rol == 'A' ):
        return render(request,"ingresar_anotacion.html", {'informacion':info, 'pk':pk, 'form_anotaciones':form_anotaciones, 'perfil':perfil})

@login_required
def crear_planilla(request):
    semana = 1
    users = Usuario.objects.all()
    print(users)
    sem=get_semana(semana)
    #turnos = turnos_base(semana, turnos)

    return render(request, "crear_planilla.html",{'semana':semana,'sem':sem, 'users':users})