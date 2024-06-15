from django.contrib import admin
from .models import Producto

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre_producto', 'descripcion_producto', 'precio_producto', 'stock_producto', 'fecha_creacion_producto', 'imagen_producto', 'estado')

admin.site.register(Producto, ProductoAdmin)