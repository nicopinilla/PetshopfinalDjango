from django.db import models

# Create your models here.
class Categoria (models.Model):
    idCategoria = models.AutoField(primary_key=True, verbose_name="Id de la categoria")
    nombreCategoria = models.CharField(max_length=80, blank=False, null=False, verbose_name="Nombre de la categoria")

    def __str__(self):
        return self.nombreCategoria

class Producto (models.Model):
    sku = models.CharField(max_length=10,primary_key=True, verbose_name="SKU")
    nombre = models.CharField(max_length=60, blank=False, null=False, verbose_name="Nombre")
    marca = models.CharField(max_length=30, null=True, blank=True,verbose_name="Marca")
    descripcion = models.CharField(max_length=100, blank=True,verbose_name="Descripcion")
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nombre