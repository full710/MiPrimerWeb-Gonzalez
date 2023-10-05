from django import forms

from . import models

class ProductosForm(forms.ModelForm):
    class Meta:
        model = models.Producto
        fields = ["nombre_producto","precio_producto"]