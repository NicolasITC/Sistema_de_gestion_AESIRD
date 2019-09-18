from django.urls import path
from . import views
import functools

from django.conf.urls import url
from django.conf import settings
from django.urls import LocalePrefixPattern, URLResolver, get_resolver, path



urlpatterns = [
    
    path('', views.home, name='home'),
    path('accounts/registrate', views.registrate, name='registrate'),
    


]
