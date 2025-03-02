from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
def tercerpaso(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_presentacionsegundopaso < 100 or
        profile.progreso_testsegundopaso < 100 
    ):
        return redirect('/segundopaso')  # Redirige de nuevo si no ha completado todo
    return render (request,'tercerpaso.html')

@login_required
def infografia_tercerpaso(request):
    return render (request,'infografia_tercerpaso.html')

@login_required
def mi_entorno_s2(request):
    return render (request,'mi_entorno_s2.html')

@login_required
def tablero_tercerpaso(request):
    return render (request,'tablero_tercerpaso.html')

@login_required
def video_tercerpaso(request):
    return render (request,'video_tercerpaso.html')

@login_required
def mi_entorno_s3(request):
    return render (request,'mi_entorno_s3.html')


@login_required
def video_consejo_tercerpaso(request):
    return render (request,'video_consejo_tercerpaso.html')

@login_required
def mi_entorno_s4(request):
    return render (request,'mi_entorno_s4.html')

@login_required
def presentacion_tercerpaso(request):
    return render(request,'presentacion_tercerpaso.html')