from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada),
    path('saludo/', views.presentacion),
]