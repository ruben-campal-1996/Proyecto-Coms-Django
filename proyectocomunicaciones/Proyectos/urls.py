from django.urls import path
from . import views

app_name= 'proyectos'

urlpatterns = [
    path('proyectos', views.proyectos, name='proyectos'),  # Cambiado de 'proyectos' a ''
    path('tareas/', views.tareas, name='tareas'),
    path('mi-perfil/', views.mi_perfil, name='mi_perfil'),
    path('add_project/', views.crear_proyecto, name='add_project'),
    path('edit_project/<int:id>/', views.editar_proyecto, name='edit_project'),
]