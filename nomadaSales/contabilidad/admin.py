from django.contrib import admin
from . import models as m

# Register your models here.
@admin.register(m.Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'stock', 
                    'precio_sugerido_compra', 'precio_sugerido_venta', 'categoria')
    search_fields = ('nombre', 'descripcion')
    list_filter = ('categoria',)