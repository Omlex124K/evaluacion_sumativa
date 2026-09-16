from django.shortcuts import render


def vista_productos(request):
    return render(request, 'catalogo/productos.html')


def vista_ofertas(request):
    return render(request, 'catalogo/ofertas.html')