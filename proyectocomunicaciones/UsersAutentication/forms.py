from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Usuario

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    rol = forms.ChoiceField(choices=Usuario.ROLES, required=True, initial='miembro')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'rol')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Crear el perfil de usuario con el rol seleccionado
            Usuario.objects.create(user=user, rol=self.cleaned_data['rol'])
        return user