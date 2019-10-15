from django.urls import path
from . import converters, views
import functools

from django.conf.urls import url
from django.conf import settings
from django.urls import LocalePrefixPattern, URLResolver, get_resolver, path, register_converter

from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.tokens import default_token_generator


register_converter(converters.NegativeIntConverter, 'negint')

urlpatterns = [
    
    path('', views.home, name='home'),
    path('accounts/registrate', views.registrate, name='registrate'),
    path('turnos/<negint:semana>/', views.planilla_turnos, name='turnos'),
    path('toma_turnos/<negint:semana>', views.toma_turnos, name='toma_turnos'),
    path('accounts/registro_completado', views.registro_completado, name='registro_completado'),
    path('asignar_turnos',views.asignar_turnos,name='asignar_turnos'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
