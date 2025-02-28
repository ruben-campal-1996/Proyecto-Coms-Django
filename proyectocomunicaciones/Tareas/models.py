from django.db import models

class Tarea(models.Model):
    ESTADOS = [
        ('sin_empezar', 'Sin empezar'),
        ('en_proceso', 'En proceso'),
        ('finalizada', 'Finalizada'),
    ]

    id_tarea = models.AutoField(primary_key=True)
    tarea = models.CharField(max_length=255)
    usuarios_asignados = models.ManyToManyField('UsersAutentication.Usuario', related_name='tareas_asignadas')
    estado = models.CharField(max_length=20, choices=ESTADOS)
    proyecto = models.ForeignKey('Proyectos.Proyecto', on_delete=models.CASCADE, related_name='tareas')

    def __str__(self):
        return self.tarea
