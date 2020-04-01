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
    path('crear_planilla/', views.crear_planilla, name='crear_planilla'),
    path('turnos/', views.turnos, name='turnos'),
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
    path('anuncios/<negint:id_anun>', views.ver_anuncios, name='ver_anuncios'),
    path('accounts/registro_completado', views.registro_completado, name='registro_completado'),
    path('finanzas',views.finanzas,name='finanzas'),
    path('perfil_user=<negint:id_perfil>', views.ver_perfil, name='ver_perfil'),
    path('editar_perfil/<int:pk>/edit/', views.editar_perfil, name='editar_perfil'),
    path('listar',views.lista,name='listar'),
    path('agregar_lista_espera',views.agregar_lista,name='agregar_lista_espera'),
    path('administracion',views.administracion,name='administracion'),
    path('ingresar_anotacion/<int:pk>',views.ingresar_anotacion,name='ingresar_anotacion'),
    path('delete/<int:persona_id>', views.delete,name="delete"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
