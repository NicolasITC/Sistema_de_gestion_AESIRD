from django.urls import path
from . import converters, views
import functools

from django.conf.urls import url
from django.conf import settings
from django.urls import LocalePrefixPattern, URLResolver, get_resolver, path, register_converter

from django.conf.urls.static import static
from django.conf import settings


register_converter(converters.NegativeIntConverter, 'negint')

urlpatterns = [
    
    path('', views.home, name='home'),
    path('accounts/registrate', views.registrate, name='registrate'),
    path('turnos/<negint:semana>/', views.planilla_turnos, name='turnos'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
