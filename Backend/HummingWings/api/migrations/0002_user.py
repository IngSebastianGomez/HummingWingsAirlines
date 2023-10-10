# Generated by Django 4.2.5 on 2023-09-30 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='Nombre(s)')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Apellido(s)')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Fecha de Nacimiento')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo')),
                ('rol', models.CharField(choices=[('Cliente', 'Cliente'), ('Administrador', 'Administrador')], default='Cliente', verbose_name='Rol')),
                ('type_document', models.CharField(choices=[('C.C.', 'C.C.'), ('C.E.', 'C.E.'), ('Pasaporte', 'Pasaporte')], default='C.C.', max_length=255, verbose_name='Tipo de documento')),
                ('document', models.CharField(max_length=255, unique=True, verbose_name='Identificación')),
                ('address', models.CharField(max_length=255, verbose_name='Dirección')),
                ('gender', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino'), ('Otro', 'Otro')], default='Otro', max_length=255, verbose_name='Género')),
                ('status', models.CharField(choices=[('pending', 'Pendiente'), ('approved', 'Aprobado'), ('rejected', 'Rechazado')], default='pending', max_length=255, verbose_name='Estado')),
                ('profile_image', models.FileField(blank=True, null=True, upload_to='user/profile_image', verbose_name='Imagen de perfil')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
            },
        ),
    ]