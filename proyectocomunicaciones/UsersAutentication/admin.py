from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('user_username', 'rol', 'proyectos_list')  # Updated fields to display
    ordering = ('user__username',)  # Sort by username from the User model

    # Custom method to display the username from the User model
    def user_username(self, obj):
        return obj.user.username
    user_username.short_description = 'Nombre de Usuario'

    # Custom method to display a list of associated projects
    def proyectos_list(self, obj):
        return ", ".join([p.nombre for p in obj.proyectos.all()])
    proyectos_list.short_description = 'Proyectos'

# Register the model with the updated admin class
admin.site.register(Usuario, UsuarioAdmin)
