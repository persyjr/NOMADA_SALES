from django.contrib import admin
from . import models as m


# Register your models here.
@admin.register(m.UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
    search_fields = ('user__username',)

@admin.register(m.Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')

@admin.register(m.Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'pais', 'phone')
    search_fields = ('name', 'email')

@admin.register(m.Asesor)
class AsesorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone')
    search_fields = ('name', 'email')
    filter_horizontal = ('cliente', 'proveedor')
