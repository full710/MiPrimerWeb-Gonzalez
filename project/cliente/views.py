
from django.shortcuts import render

from . import models

def index(request):
    contexto = {"nombre" : "El duende"}
    
    return render(request, "cliente/index.html", contexto)
