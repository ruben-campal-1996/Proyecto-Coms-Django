from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from .models import Usuario  # Importamos el modelo Usuario

# Vista principal
@login_required
def seegson_view(request):
    username = request.user.username
    return render(request, 'MainPage/Seegson.html', {'username': username})

# Página de inicio
def index(request):
    return render(request, 'index.html')

# Registro
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Crear el usuario en el sistema de autenticación de Django
            user = form.save()  # Esto ya guarda el usuario en la tabla auth_user
            
            # Opcional: Asignar un rol por defecto o desde el formulario
            rol = request.POST.get('rol', 'miembro')  # Si añades rol al formulario
            Usuario.objects.create(user=user, rol=rol)  # Crear el perfil asociado
            
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

        # Intentar encontrar el usuario por nombre de usuario o correo
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
            return redirect('seegson_view')  # Redirigir a la vista principal
        else:
            messages.error(request, "Nombre de usuario o correo electrónico y/o contraseña incorrectos")

    return render(request, 'registration/login.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('index')  # Redirigir al inicio

