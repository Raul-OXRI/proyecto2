from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Usuario(AbstractUser):

    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
        ('client', 'Cliente'),
    )

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='client')

    nombre = models.CharField(max_length=50, null=True, blank=True)
    apellido = models.CharField(max_length=50, null=True, blank=True)
    direccion = models.CharField(max_length=100, null=True, blank=True)
    telefono = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.username
    
    class Meta:
        permissions = [
            ('is_admin', 'Es administrador'),
            ('is_employee', 'Es empleado'),
            ('is_client', 'Es cliente'),
        ]
    
    