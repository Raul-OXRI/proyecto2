from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario

class UsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            # agregados por models
            'nombre', 
            'apellido', 
            'direccion', 
            'telefono', 
            # prederterminados que trae user 
            'username', 
            'password1', 
            'password2', 
            #'role'
        ]

class loginForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    password = forms.CharField(label='Contraseña', max_length=100, widget=forms.PasswordInput)


class EditRoleForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'role'
        ]