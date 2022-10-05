from itertools import pairwise
from pyexpat import model
from time import monotonic
from unittest.util import _MAX_LENGTH
from django.db import models

class Caracteristica(models.Model):
    descripcion=models.CharField(max_length=100, null=True)

    def __self__(self):
        return self.descripcion


class Categoria(models.Model):
    nombre_categoria=models.CharField(max_length=50, null=True)
    descripcion=models.CharField(max_length=100, null=True)
    caracteristicas=models.ForeignKey(Caracteristica,on_delete=models.CASCADE)


class Estado(models.Model):
    estado=models.CharField(max_length=30, null=True)


class Marca(models.Model):
    nombre_marca=models.CharField(max_length=10, null=False)


class Proveedor(models.Model):
    nombre_compania=models.CharField(max_length=40, null=True)
    pais=models.CharField(max_length=10, null=True)
    telefono=models.CharField(max_length=15, null=True)
    email=models.CharField(max_length=40, null=False)


class Producto(models.Model):
    nombre=models.CharField(max_length=25, null=True)
    precio_unidad=models.DecimalField(max_digits=5,decimal_places=2, null=True)
    descripcion=models.CharField(max_length=150, null=True)
    imagen=models.ImageField(blank=True, default='', upload_to='productos/')
    

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    marca=models.ForeignKey(Marca,on_delete=models.CASCADE)
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)



class Cliente(models.Model):
    dni=models.CharField(max_length=8,unique=True,null=True)
    nombre=models.CharField(max_length=25,null=True)
    telefono=models.CharField(max_length=15,null=True)
    region=models.CharField(max_length=25,null=True)
    correo=models.CharField(max_length=50,null=True)


class Pedido(models.Model):
    numPedido=models.CharField(max_length=10,null=True)
    fechaPedido=models.DateTimeField(auto_now_add=True,null=True)
    cantidadPedido=models.IntegerField()

    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)


class Compra(models.Model):
    unidades_pedidos=models.IntegerField(blank=True)
    forma_envio=models.CharField(max_length=20)
    fecha_llegada=models.DateTimeField(auto_now_add=True)
    importe=models.DecimalField(max_digits=5,decimal_places=2)

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)



class Venta(models.Model):
    NumOrden=models.CharField(max_length=20)
    fecha_entrega=models.DateTimeField(auto_now_add=True)
    monto=models.DecimalField(max_digits=5,decimal_places=2)

    pedido=models.ForeignKey(Pedido,on_delete=models.CASCADE)



class Inventario(models.Model):
    unidades_existencia=models.IntegerField(blank=True)
    unidades_pedidos=models.IntegerField(blank=True)

    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    venta=models.ForeignKey(Venta,on_delete=models.CASCADE)
    compra=models.ForeignKey(Compra,on_delete=models.CASCADE)



    