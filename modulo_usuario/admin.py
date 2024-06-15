from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role', 'nombre', 'apellido', 'direccion', 'telefono')}),
    )
    filter_horizontal = UserAdmin.filter_horizontal + ('groups', 'user_permissions')

admin.site.register(Usuario, UsuarioAdmin)
