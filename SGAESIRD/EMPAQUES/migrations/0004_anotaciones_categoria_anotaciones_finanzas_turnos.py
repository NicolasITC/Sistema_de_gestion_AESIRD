# Generated by Django 2.2.2 on 2019-08-29 20:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0003_auto_20190829_1935'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria_anotaciones',
            fields=[
                ('id_Categoria_anotaciones', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('nombre_anotacion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Turnos',
            fields=[
                ('id_Turnos', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('hora_inicio', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('usuario', models.ManyToManyField(blank=True, to='EMPAQUES.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Finanzas',
            fields=[
                ('id_Finanzas', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now)),
                ('comentario', models.TextField()),
                ('cantidad', models.IntegerField()),
                ('total', models.IntegerField()),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Anotaciones',
            fields=[
                ('id_Anotaciones', models.AutoField(help_text='ID', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(default=django.utils.timezone.now)),
                ('turnos_restados', models.IntegerField()),
                ('categoria_anotaciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Categoria_anotaciones')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EMPAQUES.Usuario')),
            ],
        ),
    ]
