from django.shortcuts import render, redirect

from . import forms, models

def index(request):
    
    productos = models.Producto.objects.all()    
    return render(request, "productos/index.html", {"productos": productos} )

def ingresar_producto(request):
    if request.method == "POST":
        form = forms.ProductosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos:index")
    else:
        form = forms.ProductosForm()
    return render(request, "productos/ingresar_producto.html", {"form":form})