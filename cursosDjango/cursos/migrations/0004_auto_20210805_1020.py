# Generated by Django 3.2.4 on 2021-08-05 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0003_mensajeusuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cursos',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='curso',
        ),
        migrations.RemoveField(
            model_name='cursos',
            name='phone',
        ),
    ]