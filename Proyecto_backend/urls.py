"""
URL configuration for Proyecto_backend project.

The `urlpatterns` list routes URLs to views.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('uno/', include('app_uno.urls')),
    path('dos/', include('app_dos.urls')),
    path('admin/', admin.site.urls),
]
