from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Importa las vistas de autenticación de Django

urlpatterns = [
    path('', views.index, name='index'),  # Página principal
    path('register/', views.register, name='register'),  # Página de registro
    path('login/', views.login_view, name='login'),  # Página de login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Vista de logout de Django
    path('Seegson/', views.seegson_view, name='Seegson'),
]