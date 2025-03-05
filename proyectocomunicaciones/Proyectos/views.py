from django.shortcuts import render
from .models import Proyecto
from .forms import ProyectoForm
from Tareas.models import Tarea
from UsersAutentication.models import Usuario
from django.contrib.auth.decorators import login_required


#Recuadros con la información pertinente.
@login_required
def proyectos_view(request):
    # Obtener los 5 proyectos más recientes
    proyectos_recientes = Proyecto.objects.all().order_by('-fecha_inicio')[:5]

    # Obtener las 5 tareas asignadas al usuario logueado
    usuario = request.user.usuario  # Accedemos al objeto Usuario asociado al usuario logueado
    tareas_asignadas = Tarea.objects.filter(usuarios_asignados=usuario).order_by('-id_tarea')[:5]

    # Pasar los proyectos y las tareas al template
    context = {
        'proyectos_recientes': proyectos_recientes,
        'tareas_asignadas': tareas_asignadas
    }
    
    return render(request, 'Proyectos.html', context)

@login_required
def proyectos(request):
    # Obtener los proyectos asignados al usuario
    proyectos_asignados = Proyecto.objects.filter(usuarios_asignados=request.user)  # Suponiendo que 'usuarios_asignados' es un campo en el modelo Proyecto.
    
    return render(request, 'proyectos/Proyectos.html', {'proyectos_recientes': proyectos_asignados})

@login_required
def crear_proyecto(request):
    # Verificar si el usuario es administrador
    if not request.user.is_staff:
        return redirect('proyectos:proyectos')  # Redirige si no es administrador

    if request.method == 'POST':
        # Crear el formulario solo para el proyecto
        form = ProyectoForm(request.POST)

        if form.is_valid():
            # Guardamos el proyecto
            form.save()

            # Redirigir a la página de proyectos después de guardar
            return redirect('proyectos:proyectos')

    else:
        # Si es un GET, mostramos el formulario vacío para el proyecto
        form = ProyectoForm()

    return render(request, 'Projects/add_project.html', {'form': form})


@login_required
def editar_proyecto(request, id):
    if not request.user.is_staff:
        return redirect('proyectos:proyectos')  # Redirige si no es administrador
    
    proyecto = get_object_or_404(Proyecto, pk=1)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()  # Guarda los cambios del proyecto
            return redirect('proyectos:proyectos')  # Redirige a la lista de proyectos
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'proyectos/edit_project.html', {'form': form, 'proyecto': proyecto})


# Vista para redirigir a Proyectos.html
def proyectos(request):
    return render(request, 'MainPage/Proyectos.html')

def tareas(request):
    return render(request, 'MainPage/Tareas.html')

def mi_perfil(request):
    return render(request, 'MainPage/MiPerfil.html')
