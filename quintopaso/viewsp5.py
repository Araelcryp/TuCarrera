from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
def quintopaso(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_tablerocuartopaso < 100 or
        profile.progreso_videocuartopaso < 100 or
        profile.progreso_agendacuartopaso < 100 
    ):
        return redirect('/cuartopaso')  # Redirige de nuevo si no ha completado todo
    return render (request,'quintopaso.html')

@login_required
def imagen_quintopaso(request):
    profile = request.user.profile
    profile.progreso_imagenquintopaso = 100
    profile.save()
    return render (request,'imagen_quintopaso.html')

@login_required
def tablero_quintopaso(request):
    profile = request.user.profile
    profile.progreso_tableroquintopaso = 100
    profile.save()
    return render (request,'tablero_quintopaso.html')

@login_required
def infografia_quintopaso(request):
    profile = request.user.profile
    profile.progreso_infografiaquintopaso = 100
    profile.save()
    return render (request,'infografia_quintopaso.html')