from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    ROLES = [
        ('invitado', 'Invitado'),
        ('miembro', 'Miembro'),
        ('administrador', 'Administrador'),
    ]
    
    # Vinculamos el modelo al User de Django con OneToOneField
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='miembro')

    # Relación muchos a muchos con proyectos
    proyectos = models.ManyToManyField('Proyectos.Proyecto', related_name='usuarios_asociados')

    # Relación muchos a muchos con tareas, se cambia el `related_name`
    tareas = models.ManyToManyField('Tareas.Tarea', related_name='usuarios_asignados_a_tarea')  # Cambiar related_name

    def __str__(self):
        return self.user.username  # Mostramos el nombre de usuario de Django

# Opcional: Si quieres que se cree el perfil automáticamente al crear un usuario
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.usuario.save()
