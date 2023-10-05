from django.shortcuts import render, redirect

from . import models, forms

def index(request):
    
    destinos = models.Provincias.objects.all()    
    return render(request, "envios/index.html", {"destinos": destinos} )

def agregar_destinos(request):
    if request.method == "POST":
        form = forms.DestinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("envios:index")
    else:
        form = forms.DestinoForm()
    return render(request, "envios/agregar_destinos.html", {"form":form})