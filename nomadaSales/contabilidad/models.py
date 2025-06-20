from django.db import models
from django.conf import settings

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    foto = models.ImageField(upload_to='productos/', blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    stock = models.PositiveIntegerField(default=0)
    precio_sugerido_compra = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    precio_sugerido_venta = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    categoria = models.CharField(max_length=100, blank=True, null=True)
    creado_por = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='productos_creados', null=True, blank=True
    )

    def __str__(self):
        return self.nombre

class Venta(models.Model):
    estado = models.CharField(max_length=50, choices=[
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada') 
    ], default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    url_publicacion_asociada = models.URLField(blank=True, null=True)
    cliente = models.ForeignKey('abm.Cliente', on_delete=models.CASCADE, related_name='ventas_cliente')
    asesor = models.ForeignKey('abm.Asesor', on_delete=models.CASCADE, related_name='ventas_asesor', null=True, blank=True)
    canal_de_venta = models.CharField(max_length=50, choices=[
        ('MELI', 'MELI'),
        ('DIRECTO', 'DIRECTO')
    ], default='DIRECTO')
    utilidad = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    usuario_creador = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='ventas_creadas', null=True, blank=True
    )

    def __str__(self):
        return f"Venta {self.id} - {self.estado} - {self.cliente.name}"

class ItemVentaProducto(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='items_productos')
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} - Venta {self.venta.id}"

class ItemVentaAdicional(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='items_adicionales')
    concepto = models.CharField(max_length=255)
    cantidad = models.PositiveIntegerField(default=1)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.descripcion} - Venta {self.venta.id}"