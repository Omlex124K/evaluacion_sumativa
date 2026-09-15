from django.shortcuts import render


def inicio(request):
    return render(request, 'app_dos/inicio.html', {'titulo': 'Inicio'})


def horario(request):
    return render(request, 'app_dos/horario.html', {'titulo': 'Horario'})