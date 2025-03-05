from django import forms
from .models import Proyecto
from Tareas.models import Tarea

class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = ['titulo', 'descripcion', 'fecha_inicio', 'fecha_finalizacion', 'usuarios',]

class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = ['tarea', 'estado']  # Puedes agregar más campos si es necesario

