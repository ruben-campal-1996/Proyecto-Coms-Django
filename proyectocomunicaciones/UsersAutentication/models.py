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
    proyectos = models.ManyToManyField('Proyectos.Proyecto', related_name='usuarios_asociados')  # Cambia el related_name
    
    
    def __str__(self):
        return self.nombre