# Generated by Django 2.2.2 on 2019-09-18 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0013_usuario_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default='EMPAQUES/static/media/perfil/default.png', upload_to='media/'),
        ),
    ]