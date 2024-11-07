from django.shortcuts import render

def formulario_reclamo(request):
    return render(request, 'reclamo/formulario.html')
