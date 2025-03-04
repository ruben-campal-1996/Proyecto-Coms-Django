from django.shortcuts import render
from .models import Proyecto
from Tareas.models import Tarea
from UsersAutentication.models import Usuario
from django.contrib.auth.decorators import login_required



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




# Vista para redirigir a Proyectos.html
def proyectos(request):
    return render(request, 'MainPage/Proyectos.html')

def tareas(request):
    return render(request, 'MainPage/Tareas.html')

def mi_perfil(request):
    return render(request, 'MainPage/MiPerfil.html')
