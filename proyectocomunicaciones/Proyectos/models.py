from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    usuarios = models.ManyToManyField('UsersAutentication.Usuario', related_name="proyectos_asociados")  # Cambia el related_name

    def __str__(self):
        return self.titulo
