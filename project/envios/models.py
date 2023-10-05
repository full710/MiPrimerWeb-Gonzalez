from django.db import models


class Provincias(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.nombre}"