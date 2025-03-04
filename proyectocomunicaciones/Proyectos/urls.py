from django.urls import path
from . import views

app_name= 'proyectos'

urlpatterns = [
    path('proyectos', views.proyectos, name='proyectos'),  
    path('tareas/', views.tareas, name='tareas'),
    path('mi-perfil/', views.mi_perfil, name='mi_perfil'),
]