from django.db import models

# Create your models here.

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.FloatField(max_length=10)
    
    def __str__(self) -> str:
        return self.nombre_producto