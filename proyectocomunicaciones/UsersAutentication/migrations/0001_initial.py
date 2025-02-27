# Generated by Django 5.1.6 on 2025-02-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Proyectos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('rol', models.CharField(choices=[('invitado', 'Invitado'), ('miembro', 'Miembro'), ('administrador', 'Administrador')], max_length=20)),
                ('proyectos', models.ManyToManyField(related_name='usuarios_asociados', to='Proyectos.proyecto')),
            ],
        ),
    ]
