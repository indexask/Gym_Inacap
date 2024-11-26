# Generated by Django 4.1 on 2022-11-25 06:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombre', models.CharField(max_length=30, verbose_name='')),
                ('apellido', models.CharField(max_length=30, verbose_name='')),
                ('rut', models.CharField(max_length=12, unique=True, verbose_name='')),
                ('correo', models.EmailField(max_length=70, unique=True, verbose_name='')),
                ('usuario', models.CharField(max_length=50, unique=True, verbose_name='')),
                ('fecha_nacimiento', models.DateField(max_length=50, null=True, verbose_name='')),
                ('activo', models.BooleanField(default=True)),
                ('admin', models.BooleanField(default=False)),
                ('tecnico', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Preguntas',
            fields=[
                ('idPregunta', models.AutoField(primary_key=True, serialize=False)),
                ('Titulo', models.CharField(max_length=60)),
                ('Pregunta', models.TextField()),
                ('Fecha_creacion', models.DateTimeField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Respuesta',
            fields=[
                ('idRespuesta', models.AutoField(primary_key=True, serialize=False)),
                ('Respuesta', models.TextField(verbose_name='')),
                ('FechaHora', models.DateTimeField()),
                ('Usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('id_Pregunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='online.preguntas')),
            ],
        ),
    ]