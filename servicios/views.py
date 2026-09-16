from django.shortcuts import render


def vista_lista(request):
    return render(request, 'servicios/lista.html')


def vista_contacto(request):
    return render(request, 'servicios/contacto.html')