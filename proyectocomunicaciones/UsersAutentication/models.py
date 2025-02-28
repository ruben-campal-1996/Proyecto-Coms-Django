from django.db import models

class Usuario(models.Model):
    ROLES = [
        ('invitado', 'Invitado'),
        ('miembro', 'Miembro'),
        ('administrador', 'Administrador'),
    ]
    
    id_user = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=255)
    rol = models.CharField(max_length=20, choices=ROLES)

    # Relación muchos a muchos con tareas, se cambia el `related_name`
    tareas = models.ManyToManyField('Tareas.Tarea', related_name='usuarios_asignados_a_tarea')  # Cambiar related_name

    # Relación muchos a muchos con proyectos
    proyectos = models.ManyToManyField('Proyectos.Proyecto', related_name='usuarios_asociados')

    def __str__(self):
        return self.nombre
