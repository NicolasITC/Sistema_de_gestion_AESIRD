# Generated by Django 2.2.2 on 2019-09-18 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EMPAQUES', '0012_auto_20190915_0620'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(default='perfil/default.png', upload_to='perfil/'),
        ),
    ]