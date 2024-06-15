from django.db import models

# Create your models here.
from django.db import models

# Tabla para productos
class Producto(models.Model):
    producto_id = models.AutoField(primary_key=True,)
    nombre_producto = models.CharField(max_length=50, null=True, blank=True, verbose_name="Nombre del producto")  
    descripcion_producto = models.CharField(max_length=50, null=True, blank=True, verbose_name="Descripción del producto") 
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio del producto")
    stock_producto = models.IntegerField(null=True, blank=True, verbose_name="Cantidad del producto")
    fecha_creacion_producto = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de ingreso del producto")  
    imagen_producto = models.ImageField(upload_to='productos_imagenes/', verbose_name="Imagen del producto")
    estado = models.CharField(max_length=50, default='1')

    def __str__(self):
        return self.nombre_producto
