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
    profile = request.user.profile
    profile.progreso_infografiatercerpaso = 100
    profile.save()
    return render (request,'infografia_tercerpaso.html')

@login_required
def mi_entorno_s2(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_infografiatercerpaso < 100
    ):
        return redirect('/tercerpaso')  # Redirige de nuevo si no ha completado todo
    
    return render (request,'mi_entorno_s2.html')

@login_required
def tablero_tercerpaso(request):
    profile = request.user.profile
    profile.progreso_tablerotercerpaso = 100
    profile.save()
    return render (request,'tablero_tercerpaso.html')

@login_required
def video_tercerpaso(request):
    profile = request.user.profile
    profile.progreso_videotercerpaso = 100
    profile.save()
    return render (request,'video_tercerpaso.html')


@login_required
def video_consejo_tercerpaso(request):
    profile = request.user.profile
    profile.progreso_videoconsejotercerpaso = 100
    profile.save()
    return render (request,'video_consejo_tercerpaso.html')


@login_required
def presentacion_tercerpaso(request):
    profile = request.user.profile
    profile.progreso_presentaciontercerpaso = 100
    profile.save()
    return render(request,'presentacion_tercerpaso.html')