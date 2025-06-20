from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http import HttpRequest, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from . import models as m
from . import forms as f
from typing import Any


# Create your views here.
class Crear_producto(generic.FormView):
    model = m.Producto
    form_class = f.CreateProducto
    template_name = 'producto_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'productos': m.Producto.objects.all(),
            'form': self.get_form(),
        })
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        nombre = form.cleaned_data["nombre"]
        descripcion = form.cleaned_data["descripcion"]
        foto = form.cleaned_data["foto"]
        stock = form.cleaned_data["stock"]
        precio_sugerido_compra = form.cleaned_data["precio_sugerido_compra"]
        precio_sugerido_venta = form.cleaned_data["precio_sugerido_venta"]
        categoria = form.cleaned_data["categoria"]
        producto = m.Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            foto=foto,
            stock=stock,
            precio_sugerido_compra=precio_sugerido_compra,
            precio_sugerido_venta=precio_sugerido_venta,
            categoria=categoria,
            creado_por=self.request.user)
        producto.save()
        return HttpResponseRedirect(reverse_lazy('contabilidad:crear_producto'))
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print('CREATE')
            return self.form_valid(form)
        else:
            print('NO SE CREO')
            return self.form_invalid(form)

class editar_producto(generic.UpdateView):
    model = m.Producto
    form_class = f.CreateProducto
    template_name = 'producto_list.html'
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'productos': m.Producto.objects.all(),
            'form2': self.get_form(),
        })
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        nombre = form.cleaned_data["nombre"]
        descripcion = form.cleaned_data["descripcion"]
        foto = form.cleaned_data["foto"]
        stock = form.cleaned_data["stock"]
        precio_sugerido_compra = form.cleaned_data["precio_sugerido_compra"]
        precio_sugerido_venta = form.cleaned_data["precio_sugerido_venta"]
        categoria = form.cleaned_data["categoria"]
        producto = m.Producto.objects.get(id=self.kwargs['pk'])
        producto.nombre = nombre
        producto.descripcion = descripcion
        producto.foto = foto
        producto.stock = stock
        producto.precio_sugerido_compra = precio_sugerido_compra
        producto.precio_sugerido_venta = precio_sugerido_venta
        producto.categoria = categoria
        producto.creado_por = self.request.user
        producto.save()
        return HttpResponseRedirect(reverse_lazy('contabilidad:crear_producto'))
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            print('UPDATE')
            return self.form_valid(form)
        else:
            print('NO SE CREO')
            return self.form_invalid(form)

class delete_producto(generic.DeleteView):
    model = m.Producto
    template_name = 'producto_list.html'
    success_url = reverse_lazy('contabilidad:crear_producto')
    form_class = f.CreateProducto

    def get_context_data(self, **kwargs):
        kwargs.update({
            'productos': m.Producto.objects.all(),
            'form': self.get_form(),
        })
        return super().get_context_data(**kwargs)
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        producto = self.get_object()
        producto.delete()
        return HttpResponseRedirect(self.success_url)

class listar_productos(generic.TemplateView):
    model = m.Producto
    template_name = 'producto_list.html'
    form_class = f.CreateProducto
    
    def get_context_data(self, **kwargs):
        kwargs.update({
            'productos': m.Producto.objects.all(),
            'form': self.get_form()
        })
        return super().get_context_data(**kwargs)
    def get_form(self):
        return self.form_class(self.request.POST or None, self.request.FILES or None)