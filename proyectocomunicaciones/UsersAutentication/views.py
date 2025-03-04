from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth import logout
from .forms import CustomUserCreationForm  # Importa logout desde django.contrib.auth
from django.contrib.auth.decorators import login_required  # Necesario para usar @login_required

@login_required  # Aseguramos que solo los usuarios logueados puedan acceder
def seegson_view(request):
    # Obtenemos el nombre de usuario
    username = request.user.username
    
    # Renderizamos la página Seegson.html y pasamos el nombre de usuario
    return render(request, 'Seegson.html', {'username': username})  # Redirige a Seegson.html

# Registro
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Crear el nuevo usuario
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'Cuenta creada con éxito. ¡Ya puedes iniciar sesión!')
            return redirect('login')  # Redirigir al login
    else:
        form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

# Login
def login_view(request):
    if request.method == 'POST':
        username_or_email = request.POST.get('username_or_email')  # Obtener el valor del campo de texto
        password = request.POST.get('password')  # Obtener la contraseña

        # Verificar si el valor no está vacío
        if not username_or_email or not password:
            messages.error(request, "Por favor, ingrese tanto el nombre de usuario/correo y la contraseña.")
            return redirect('login')  # Redirige a la página de login si hay un campo vacío

        # Intentar encontrar el usuario por nombre de usuario o correo electrónico
        user = None

        # Verificar si el valor ingresado es un correo electrónico
        if '@' in username_or_email:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                user = None
        else:
            # Si no es un correo, buscar por nombre de usuario
            user = User.objects.filter(username=username_or_email).first()

        # Si se encuentra un usuario y la contraseña es correcta
        if user and user.check_password(password):
            login(request, user)
            messages.success(request, "Bienvenido de nuevo!")
            return redirect('Seegson')  # O donde quieras redirigir
        else:
            messages.error(request, "Nombre de usuario o correo electrónico y/o contraseña incorrectos")

    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)  # Cierra la sesión del usuario
    return redirect('Templates/index.html')

@login_required  # Aseguramos que solo los usuarios logueados puedan acceder
def seegson_view(request):
    username = request.user.username
    return render(request, 'MainPage/Seegson.html', {'username': username})

