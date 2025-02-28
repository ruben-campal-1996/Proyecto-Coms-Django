from django.db import models

# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    usuarios = models.ManyToManyField('UsersAutentication.Usuario', related_name="proyectos_asociados")  # Relación muchos a muchos con Proyectos
    #tareas = models.ManyToManyField('Tarea', related_name="tareas_asociadas")  # Relación muchos a muchos con Tarea

'''Si da error cambiar nombre para que usuarios y tareas tengan el mismo related_name="proyectos_asociados"'''
    def __str__(self):
        return self.titulo