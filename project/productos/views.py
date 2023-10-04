from django.shortcuts import render



def index(request):
    contexto = {"nombre" : "Productos"}
    return render(request, "productos/index.html", contexto)