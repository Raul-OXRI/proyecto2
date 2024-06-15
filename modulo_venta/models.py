from django.db import models
from modulo_producto.models import Producto
from modulo_usuario.models import Usuario

# Modelo de Venta
class Venta(models.Model):
    venta_id = models.AutoField(primary_key=True)
    empleado = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_venta = models.DateField(auto_now_add=True)
    total_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Venta {self.venta_id} - {self.fecha_venta}"

# Modelo de DetalleVenta
class DetalleVenta(models.Model):
    detalle_venta_id = models.AutoField(primary_key=True)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Detalle Venta {self.detalle_venta_id} - Venta {self.venta.venta_id}"
