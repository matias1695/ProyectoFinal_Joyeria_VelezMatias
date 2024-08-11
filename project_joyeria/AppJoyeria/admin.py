from django.contrib import admin
from .models import *
# Register your models here.

class ArticuloAdmin(admin.ModelAdmin):
    list_display =("idArt","nomArt","material")
    list_filter = ("idArt","nomArt","material")
    ordering = ("nomArt", "precioArt")

admin.site.register(Articulo,ArticuloAdmin)

class ClienteAdmin(admin.ModelAdmin):
    list_display=("nombre","apellido")
    ordering = ("apellido", )
    
admin.site.register(Cliente,ClienteAdmin)
    
class VentaAdmin(admin.ModelAdmin):
    list_display =("idVenta","idCliente","idArt","cant","montoVta","tipoPago")
    list_filter = ("tipoPago",)
    ordering = ("tipoPago", )
    
admin.site.register(Venta,VentaAdmin)

class TareaAdmin(admin.ModelAdmin):
    list_display=('titulo','fecha')
    ordering=('fecha',)
    
admin.site.register(Tarea,TareaAdmin)