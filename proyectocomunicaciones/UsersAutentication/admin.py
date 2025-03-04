# UsersAutentication/admin.py
from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id_user', 'nombre', 'rol']  # Muestra el id, nombre y rol de los usuarios en el listado
    list_filter = ['rol']  # Permite filtrar los usuarios por rol
    search_fields = ['nombre']  # Permite buscar usuarios por nombre
    ordering = ['id_user']  # Ordena por el campo id_user de manera ascendente

# Registra el modelo Usuario y su configuración en el panel de administración
admin.site.register(Usuario, UsuarioAdmin)
