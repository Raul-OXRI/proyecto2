from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login as django_login, authenticate 
from .forms import UsuarioForm, loginForm, EditRoleForm
from .models import Usuario


# Create your views here.

def singup (request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)    
            django_login(request, user)
            return redirect('start')
    else:
        form = UsuarioForm()
    return render(request, 'singup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                django_login(request, user)
                return redirect('start')
            else:
                form.add_error(None, 'Usuario o contraseña incorrectos')
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def list_users(request):
    users = Usuario.objects.all()
    return render(request, 'list_users.html', {'users': users})

def edit(request, user_id):
    user = get_object_or_404(Usuario, id=user_id)
    if request.method == 'POST':
        form = EditRoleForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = EditRoleForm(instance=user)
    return render(request, 'edit.html', {'form': form, 'user': user})