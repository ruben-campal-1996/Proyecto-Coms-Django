from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    ROLES = [
        ('invitado', 'Invitado'),
        ('miembro', 'Miembro'),
        ('administrador', 'Administrador'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    rol = models.CharField(max_length=20, choices=ROLES, default='invitado')
    proyectos = models.ManyToManyField('Proyectos.Proyecto', related_name='usuarios_asociados', blank=True)
    tareas = models.ManyToManyField('Tareas.Tarea', related_name='usuarios_asignados_a_tarea', blank=True)

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance, rol='invitado')  # Rol por defecto 'invitado'

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.usuario.save()  # Guardar cambios si el perfil ya existe
    except Usuario.DoesNotExist:
        pass  # Si no existe, no hacemos nada (ya se creó en create_user_profile)