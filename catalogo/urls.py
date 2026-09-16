from django.urls import path
from . import views

urlpatterns = [
    path("productos/", views.vista_productos),
    path("ofertas/", views.vista_ofertas),
]