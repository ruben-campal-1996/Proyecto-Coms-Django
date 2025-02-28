from django.db import models

class Proyecto(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()

    # Relación muchos a muchos con usuarios
    usuarios = models.ManyToManyField('UsersAutentication.Usuario', related_name="proyectos_asociados")

    # Relación muchos a muchos con tareas
    tareas = models.ManyToManyField('Tareas.Tarea', related_name="proyectos_asociados")

    def __str__(self):
        return self.titulo

    def calcular_porcentaje_completado(self):
        # Obtener todas las tareas asociadas al proyecto
        total_tareas = self.tareas.count()
        
        if total_tareas == 0:
            return 0  # Si no hay tareas, el porcentaje de completado es 0%

        # Contar cuántas tareas están finalizadas
        tareas_completadas = self.tareas.filter(estado='finalizada').count()

        # Calcular el porcentaje
        porcentaje_completado = (tareas_completadas / total_tareas) * 100
        return round(porcentaje_completado, 2)  # Redondear a dos decimales
