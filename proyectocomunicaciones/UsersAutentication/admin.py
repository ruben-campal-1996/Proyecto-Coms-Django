from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'rol', 'proyectos_list', 'tareas_list')
    ordering = ('user__username',)
    filter_horizontal = ('proyectos', 'tareas')  # Mejora la interfaz para campos muchos a muchos

    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Nombre de Usuario'

    def proyectos_list(self, obj):
        return ", ".join([p.nombre for p in obj.proyectos.all()])
    proyectos_list.short_description = 'Proyectos'

    def tareas_list(self, obj):
        return ", ".join([t.tarea for t in obj.tareas.all()])
    tareas_list.short_description = 'Tareas'

admin.site.register(Usuario, UsuarioAdmin)
