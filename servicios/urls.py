from django.urls import path
from . import views

urlpatterns = [
    path("lista/", views.vista_lista),
    path("contacto/", views.vista_contacto),
]