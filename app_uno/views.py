from django.shortcuts import render


def portada(request):
    return render(request, 'app_uno/portada.html', {'titulo': 'Portada'})


def presentacion(request):
    return render(request, 'app_uno/presentacion.html', {'titulo': 'Presentación'})