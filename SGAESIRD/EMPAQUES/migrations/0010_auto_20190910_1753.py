# Generated by Django 2.2.2 on 2019-09-10 17:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0009_auto_20190910_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='activo',
            field=models.CharField(choices=[('A', 'Activo'), ('V', 'Vacaciones'), ('S', 'Suspendido'), ('E', 'Eliminado')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cant_turnos_disponibles',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='carrera',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='fecha_ingreso',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('A', 'Administrador'), ('E', 'Empaque'), ('R', 'Reemplazo')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='rut',
            field=models.CharField(choices=[('A', 'Administrador'), ('E', 'Empaque'), ('R', 'Reemplazo')], max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='universidad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Universidades'),
        ),
    ]