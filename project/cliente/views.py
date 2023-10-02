
from django.shortcuts import render

def index(request):
    contexto = {"nombre" : "El duende"}
    return render(request, "cliente/index.html", contexto)
