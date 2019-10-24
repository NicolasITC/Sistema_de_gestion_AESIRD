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
    path('accounts/reset-password/', auth_views.PasswordResetView.as_view(
      template_name='reset_password.html',
      html_email_template_name='reset_password_email.html',
      success_url='done',
      token_generator=default_token_generator),
    name='reset_password'
    ),
    path('accounts/reset-password-confirm/<str:uidb64>/<str:token>/', auth_views.PasswordResetConfirmView.as_view(
      template_name='reset_password_update.html', 
      post_reset_login=True,
      post_reset_login_backend='django.contrib.auth.backends.ModelBackend',
      token_generator=default_token_generator,
      success_url=settings.LOGIN_REDIRECT_URL),
    name='passwordResetConfirm'
    ),
    path('accounts/reset-password/done', auth_views.PasswordResetDoneView.as_view(
      template_name='reset_password_done.html'),
    name='passwordResetDone'
    ),
    path('anuncios', views.ver_anuncios, name='ver_anuncios'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
