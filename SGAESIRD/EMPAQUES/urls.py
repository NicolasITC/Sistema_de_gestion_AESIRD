from django.urls import path
from . import views
import functools

from django.conf.urls import url
from django.conf import settings
from django.urls import LocalePrefixPattern, URLResolver, get_resolver, path

from django.conf.urls.static import static
from django.conf import settings




urlpatterns = [
    
    path('', views.home, name='home'),
    path('accounts/registrate', views.registrate, name='registrate'),
    


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
