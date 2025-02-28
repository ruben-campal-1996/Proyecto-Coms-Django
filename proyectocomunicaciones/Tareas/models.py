from django.db import models

class Tarea(models.Model):
    ESTADOS = [
        ('sin_empezar', 'Sin empezar'),
        ('en_proceso', 'En proceso'),
        ('finalizada', 'Finalizada'),
    ]

    id_tarea = models.AutoField(primary_key=True)
    tarea = models.CharField(max_length=255)
    usuarios_asignados = models.ManyToManyField('UsersAutentication.Usuario', related_name='tareas_asignadas_usuario')  # Cambiar related_name
    estado = models.CharField(max_length=20, choices=ESTADOS)

    # Relación de clave foránea con Proyecto
    proyecto = models.ForeignKey('Proyectos.Proyecto', on_delete=models.CASCADE, related_name="tareas_del_proyecto")

    def __str__(self):
        return self.tarea

