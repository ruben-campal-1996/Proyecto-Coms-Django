# Generated by Django 5.1.6 on 2025-02-28 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tareas', '0001_initial'),
        ('UsersAutentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='tareas',
            field=models.ManyToManyField(related_name='usuarios_asignados_a_tarea', to='Tareas.tarea'),
        ),
    ]
