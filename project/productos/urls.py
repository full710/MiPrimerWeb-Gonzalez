from django.urls import path
from . import views

app_name = "productos"

urlpatterns = [
    path("", views.index, name="index"),    
    path("ingresar_producto/", views.ingresar_producto, name="ingresar_producto"),
]
