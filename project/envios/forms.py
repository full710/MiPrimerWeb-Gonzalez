from django import forms

from . import models

class DestinoForm(forms.ModelForm):
    class Meta:
        model = models.Provincias
        fields = ["nombre"]