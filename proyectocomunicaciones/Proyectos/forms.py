from django import forms
from .models import Proyecto

#Simplificación para la creación y edición de proyectos.

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_finalizacion']
