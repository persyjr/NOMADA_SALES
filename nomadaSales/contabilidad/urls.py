# Description: URLs for the inspecciones app
""" Inspecciones URLs """

from django.urls import path
from . import views

app_name = 'contabilidad'
urlpatterns = [
    path('crear_producto/', views.Crear_producto.as_view(), name='crear_producto'),
    path('editar_producto/<int:pk>/', views.editar_producto.as_view(), name='editar_producto'),
    path('eliminar_producto/<int:pk>/', views.delete_producto.as_view(), name='eliminar_producto'),
    # Add more paths as needed
    ]
    #path('listar_productos/', views.listar_productos.as_view(), name='listar_productos'),
