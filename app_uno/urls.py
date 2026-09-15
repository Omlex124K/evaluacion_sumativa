from django.urls import path
from . import views

urlpatterns = [
    path('', views.portada, name='portada'),
    path('saludo/', views.presentacion, name='presentacion'),
]