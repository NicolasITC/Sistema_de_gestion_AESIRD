# Generated by Django 3.0.4 on 2020-03-25 23:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0016_auto_20191014_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='anotaciones',
            name='fecha_termino_sancion',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
