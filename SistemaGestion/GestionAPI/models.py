from enum import unique
from itertools import pairwise
from pyexpat import model
from time import monotonic
from unittest.util import _MAX_LENGTH
from django.db import models

class Caracteristica(models.Model):
    descripcion=models.CharField(max_length=250, null=True)
    def __str__ (self):
        return self.descripcion


class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50, null=True)
    caracteristica=models.ForeignKey(Caracteristica,on_delete=models.CASCADE)
    def __str__ (self):
        return self.nombre_categoria


class Estado(models.Model):
    estado=models.CharField(max_length=30, null=True)

    def __str__ (self):
        return self.estado


class Marca(models.Model):
    nombre_marca=models.CharField(max_length=10, null=False)
    def __str__ (self):
        return self.nombre_marca
    


class Proveedor(models.Model):
    nombre_proveedor=models.CharField(max_length=40, null=True)
    pais=models.CharField(max_length=10, null=True)
    telefono=models.CharField(max_length=15, null=True)
    email=models.CharField(max_length=40, null=False)
    def __str__ (self):
        return self.nombre_proveedor


class Cliente(models.Model):
    dni=models.CharField(max_length=8,unique=True,null=True)
    nombre=models.CharField(max_length=25,null=True)
    telefono=models.CharField(max_length=15,null=True)
    region=models.CharField(max_length=25,null=True)
    correo=models.CharField(max_length=50,null=True)

    def __str__ (self):
        return self.nombre

    
class Producto(models.Model):
    codigo_producto=models.CharField(max_length=25,unique=True, null=True)
    nombre=models.CharField(max_length=25, null=True)
    precio_unidad=models.DecimalField(max_digits=5,decimal_places=2, null=True)
    imagen=models.ImageField(blank=True, default='', upload_to='productos/')
    

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)

    def __str__ (self):
        return self.codigo_producto

class Pedido(models.Model):
    numPedido=models.CharField(max_length=10,unique=True,null=True)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    
    def __str__ (self):
        return self.numPedido

class Compra(models.Model):
    nro_compra=models.IntegerField()
    factura=models.CharField(max_length=20)
    monto=models.DecimalField(max_digits=5,decimal_places=2)
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)

    def __str__ (self):
        return self.nro_compra


class Detalle_compra(models.Model):
    fechaEntrega=models.DateTimeField(auto_now_add=True)
    precio_unidad=models.DecimalField(max_digits=5,decimal_places=2)
    cantidad=models.IntegerField()
    sub_total=models.DecimalField(max_digits=5,decimal_places=2)

    nro_comp=models.ForeignKey(Compra,on_delete=models.CASCADE)
    nombre_producto=models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__ (obj):
        return obj.cantidad

class Forma_envio(models.Model):
    modalidad=models.CharField(max_length=20)

    def __str__ (self):
        return self.modalidad

class Venta(models.Model):
    NumOrden=models.CharField(max_length=20,unique=True,null=True)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    numPedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    modalidad=models.ForeignKey(Forma_envio,on_delete=models.CASCADE)

    def __str__ (self):
        return self.NumOrden

class Detalle_venta(models.Model):
    fecha_venta=models.DateTimeField(auto_now_add=True,null=True)
    subTotal=models.DecimalField(max_digits=5,decimal_places=2)
    descuento=models.CharField(max_length=4)
    cantidad=models.IntegerField()
    venta=models.ForeignKey(Venta,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)

    def __str__ (self):
        return self.cantidad
    

class Movimiento(models.Model):
    tipo=models.CharField(max_length=25)

    def __str__ (self):
        return self.tipo

class Inventario(models.Model):
    unidades_existencia=models.IntegerField()
    unidades_pedidos=models.IntegerField()
    stock=models.IntegerField()
    fechaHora=models.DateTimeField(auto_now_add=True,null=True)

    detalle_venta=models.ForeignKey(Detalle_venta, on_delete=models.CASCADE)
    detalle_compra=models.ForeignKey(Detalle_compra, on_delete=models.CASCADE)
    movimiento=models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    codigo_producto=models.ForeignKey(Producto, on_delete=models.CASCADE)

