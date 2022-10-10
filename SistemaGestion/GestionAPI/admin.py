from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Caracteristica)
admin.site.register(models.Categoria)
admin.site.register(models.Estado)
admin.site.register(models.Marca)
admin.site.register(models.Proveedor)
admin.site.register(models.Producto)
admin.site.register(models.Cliente)
admin.site.register(models.Pedido)
admin.site.register(models.Compra)
admin.site.register(models.Venta)
admin.site.register(models.Detalle_compra)
admin.site.register(models.Forma_envio)
admin.site.register(models.Detalle_venta)
admin.site.register(models.Movimiento)
admin.site.register(models.Inventario)
