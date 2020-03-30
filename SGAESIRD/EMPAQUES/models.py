from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.


class Universidades(models.Model):
	nombre=models.CharField(max_length=200)
	def __str__(self):
		return self.nombre

class Usuario(models.Model):
	OPCIONES_ROL = (
        ('A','Administrador'),
        ('E','Empaque'),
        ('R','Reemplazo'),
    )
	OPCIONES_ACTIVIDAD = (
		('A','Activo'),
		('V','Vacaciones'),	
		('S','Suspendido'),
		('E','Eliminado')
	)
	id_Usuario = models.AutoField(primary_key=True, help_text="ID")
	usuario = models.OneToOneField(User, on_delete=models.CASCADE)
	rut = models.CharField(max_length=10, null=True)
	rol = models.CharField(max_length=1, choices=OPCIONES_ROL, null=True)
	fecha_ingreso = models.DateTimeField(default=timezone.now, null=True)
	carrera = models.CharField(max_length=200, null=True)
	universidad = models.ForeignKey(Universidades, on_delete=models.CASCADE, null=True)
	activo = models.CharField(max_length=1, choices=OPCIONES_ACTIVIDAD, null=True)
	telefono = models.CharField(max_length=12, null=True)
	cant_turnos_disponibles = models.IntegerField(null=True)
	foto = models.ImageField(upload_to='perfil/', default='perfil/default.png')

	def __str__(self):
		return self.usuario.first_name + " " + self.usuario.last_name
	def get_date(self):
		return self.created_date

class Toma_turnos(models.Model):
	fecha_inicio = models.DateTimeField()
	lugar_reunion = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return "Fecha inicio: " + str(self.fecha_inicio) + "Lugar reunion: " + str(self.lugar_reunion)
class Categoria_anotaciones(models.Model):
	id_Categoria_anotaciones = models.AutoField(primary_key=True, help_text="ID")
	nombre_anotacion = models.CharField(max_length=200)
	def __str__(self):
		return self.nombre_anotacion

class Anotaciones(models.Model):
	id_Anotaciones = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateTimeField(default=timezone.now)
	categoria_anotaciones = models.ForeignKey(Categoria_anotaciones, on_delete=models.CASCADE)
	turnos_restados = models.IntegerField()
	fecha_termino_sancion = models.DateField(default = timezone.now)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.fecha) + " " + str(self.categoria_anotaciones) + " " + str(self.usuario.usuario)



		
class Turno(models.Model):
	id_Turnos = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	emp01=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='01+', blank=True, null=True)
	emp02=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='02+', blank=True, null=True)
	emp03=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='03+', blank=True, null=True)
	emp04=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='04+', blank=True, null=True)
	emp05=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='05+', blank=True, null=True)
	emp06=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='06+', blank=True, null=True)
	emp07=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='07+', blank=True, null=True)
	emp08=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='08+', blank=True, null=True)
	emp09=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='09+', blank=True, null=True)
	emp10=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='10+', blank=True, null=True)
	emp11=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='11+', blank=True, null=True)
	emp12=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='12+', blank=True, null=True)
	emp13=models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='13+', blank=True, null=True)
	def __str__(self):
		return str(self.fecha) 


class Finanzas(models.Model):
	id_Finanzas = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	comentario = models.TextField()
	cantidad = models.IntegerField()
	total = models.IntegerField()
	responsable = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	def __str__(self):
		return self.fecha.strftime("%d/%m/%Y") + " " + self.comentario + " " + str(self.cantidad)

class Anuncios(models.Model):
	id_Anuncios = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	usuario = models.ForeignKey(Usuario, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.fecha) + " " + self.titulo + " " + str(self.id_Anuncios)

class Comentarios(models.Model):
	id_Comentarios = models.AutoField(primary_key=True, help_text="ID")
	fecha = models.DateField(default=timezone.now)
	contenido = models.TextField()
	anuncio = models.ForeignKey(Anuncios, on_delete=models.CASCADE)
	usuario = models.ForeignKey(Usuario, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return str(self.fecha) + " " + self.anuncio.titulo  + " " + str(self.anuncio.id_Anuncios)

class Lista_de_Espera(models.Model):
	id_Lista_de_Espera = models.AutoField(primary_key=True, help_text="ID")
	fecha_ingreso = models.DateTimeField(default=timezone.now)
	rut = models.CharField(max_length=200)
	nombre = models.CharField(max_length=200)
	apellido = models.CharField(max_length=200)
	carrera = models.CharField(max_length=200)
	universidad = models.ForeignKey(Universidades, on_delete=models.CASCADE)
	telefono = models.CharField(max_length=12)
	def __str__(self):
		return self.nombre + " " + self.apellido

class Mensaje_inicio(models.Model):
	titulo = models.CharField(max_length=50)
	mensaje = models.CharField(max_length=200)
	fecha = models.DateField(default=timezone.now)