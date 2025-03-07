from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from .models import Proyecto
from .forms import ProyectoForm
from Tareas.models import Tarea
from UsersAutentication.models import Usuario

# Vista principal de proyectos (lista de proyectos asignados)
@login_required
def proyectos(request):
    # Obtener los proyectos asignados al usuario logueado a través de la relación ManyToMany en Usuario
    usuario = request.user.usuario
    proyectos_asignados = usuario.proyectos.all().order_by('-fecha_inicio')[:5]  # Últimos 5 proyectos

    # Obtener las tareas asignadas al usuario logueado
    tareas_asignadas = Tarea.objects.filter(usuarios_asignados=usuario).order_by('-id_tarea')[:5]

    context = {
        'proyectos_recientes': proyectos_asignados,
        'tareas_asignadas': tareas_asignadas,
    }
    return render(request, 'MainPage/Proyectos.html', context)

# Vista para crear un proyecto (equivalente a 'add_project')
@login_required
def crear_proyecto(request):
    # Verificar si el usuario tiene permisos de administrador
    if request.user.usuario.rol != 'administrador':  # Cambié is_staff por rol de administrador
        messages.error(request, "No tienes permiso para crear proyectos.")
        return redirect('proyectos:proyectos')

    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save()
            messages.success(request, f"Proyecto {proyecto.titulo} creado con éxito.")
            return redirect('proyectos:proyectos')
    else:
        form = ProyectoForm()

    return render(request, 'Projects/add_project.html', {'form': form})

# Vista para editar un proyecto
@login_required
def editar_proyecto(request, id):
    # Verificar si el usuario tiene permisos de administrador
    if request.user.usuario.rol != 'administrador':  # Cambié is_staff por rol de administrador
        messages.error(request, "No tienes permiso para editar proyectos.")
        return redirect('proyectos:proyectos')

    # Obtener el proyecto por ID
    proyecto = get_object_or_404(Proyecto, pk=id)  # Corregí 'pk=1' por 'pk=id' para usar el parámetro dinámico

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, f"Proyecto {proyecto.titulo} actualizado con éxito.")
            return redirect('proyectos:proyectos')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'Projects/edit_project.html', {'form': form, 'proyecto': proyecto})

# Vistas placeholder para otras secciones
@login_required
def tareas(request):
    return render(request, 'proyectos/Tareas.html')

@login_required
def mi_perfil(request):
    return render(request, 'proyectos/MiPerfil.html')

# Vista eliminada: proyectos_view (duplicada con proyectos)
# Si necesitas una vista diferente para MainPage/Proyectos.html, podemos añadirla por separado