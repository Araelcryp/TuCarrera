from django.shortcuts import render

# Create your views here.

def home(request):
    return render (request, 'home.html')

def aboutprogram(request):
    return render (request, 'about-program.html')

def tutor(request):
    return render (request, 'tutor.html')

def areas_profesionales(request):
    return render (request, 'areas_profesionales.html')

def directorio_universidades(request):
    return render (request, 'directorio_universidades.html')

def becas_vigentes(request):
    return render (request, 'becas_vigentes.html')