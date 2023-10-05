from django.urls import path
from . import views

app_name = "envios"

urlpatterns = [
    path("", views.index, name="index"),
    path("agregar_destinos/", views.agregar_destinos, name="agregar_destinos"),    
]