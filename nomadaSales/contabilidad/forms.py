from django import forms
from . import models as m

class CreateProducto(forms.ModelForm):
    class Meta:
        model = m.Producto
        fields = ['nombre', 'descripcion', 'foto', 'precio', 'stock',
                  'precio_sugerido_compra', 'precio_sugerido_venta', 'categoria']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["nombre"].widget.attrs.update({"class": "text-info"})
        self.fields["descripcion"].widget.attrs.update({"class": "text-info"})
        self.fields["precio"].widget.attrs.update({"class": "text-info"})
        self.fields["stock"].widget.attrs.update({"class": "text-info"})
        self.fields["precio_sugerido_compra"].widget.attrs.update({"class": "text-info"})
        self.fields["precio_sugerido_venta"].widget.attrs.update({"class": "text-info"})
        self.fields["categoria"].widget.attrs.update({"class": "text-info"})
        