# Generated by Django 5.1.6 on 2025-02-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Proyectos', '0001_initial'),
        ('UsersAutentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='usuarios',
            field=models.ManyToManyField(related_name='proyectos_asociados', to='UsersAutentication.usuario'),
        ),
    ]
