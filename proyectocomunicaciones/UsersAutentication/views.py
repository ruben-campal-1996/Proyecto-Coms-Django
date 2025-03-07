from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Usuario

# Vista principal
@login_required
def seegson_view(request):
    username = request.user.username
    return render(request, 'MainPage/Seegson.html', {'username': username})

# Página de inicio
def index(request):
    return render(request, 'index.html')

# Registro de usuarios (sin creación manual de Usuario)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Crea el usuario en auth_user
            # Las señales ya crean el perfil Usuario con rol 'invitado'
            messages.success(request, 'Cuenta creada con éxito. ¡Ya puedes iniciar sesión!')
            return redirect('login')
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')
        password = request.POST.get('password')

        if not username_or_email or not password:
            messages.error(request, "Por favor, ingrese tanto el nombre de usuario/correo como la contraseña.")
            return redirect('login')

        user = None
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user = None
        else:
            user = User.objects.filter(username=username_or_email).first()

        if user and user.check_password(password):
            login(request, user)
            messages.success(request, "Bienvenido de nuevo!")
            return redirect('Seegson')
        else:
            messages.error(request, "Nombre de usuario o correo electrónico y/o contraseña incorrectos")

    return render(request, 'registration/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('index')

# Vista para administradores: Crear usuarios
@login_required
def admin_create_user(request):
    if request.user.usuario.rol != 'administrador':
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('seegson_view')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        rol = request.POST.get('rol')  # El administrador elige el rol
        if form.is_valid() and rol in dict(Usuario.ROLES):
            user = form.save()
            Usuario.objects.create(user=user, rol=rol)  # Asigna el rol elegido
            messages.success(request, f"Usuario {user.username} creado con éxito.")
            return redirect('admin_manage_users')
    else:
        form = CustomUserCreationForm()

    return render(request, 'admin/create_user.html', {'form': form, 'roles': Usuario.ROLES})

# Vista para administradores: Gestionar roles de usuarios
@login_required
def admin_manage_users(request):
    if request.user.usuario.rol != 'administrador':
        messages.error(request, "No tienes permiso para acceder a esta página.")
        return redirect('seegson_view')

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        new_rol = request.POST.get('rol')
        try:
            usuario = Usuario.objects.get(user__id=user_id)
            if new_rol in dict(Usuario.ROLES):
                usuario.rol = new_rol
                usuario.save()
                messages.success(request, f"Rol de {usuario.user.username} actualizado a {new_rol}.")
            else:
                messages.error(request, "Rol no válido.")
        except Usuario.DoesNotExist:
            messages.error(request, "Usuario no encontrado.")
        return redirect('admin_manage_users')

    usuarios = Usuario.objects.all()  # Lista de todos los usuarios
    return render(request, 'admin/manage_users.html', {'usuarios': usuarios, 'roles': Usuario.ROLES})

