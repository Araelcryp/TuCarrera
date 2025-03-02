from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required
def sextopaso(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_imagenquintopaso < 100 or
        profile.progreso_tableroquintopaso < 100 or
        profile.progreso_infografiaquintopaso < 100 
    ):
        return redirect('/quintopaso')  # Redirige de nuevo si no ha completado todo
    return render (request,'sextopaso.html')

@login_required
def tablero_sextopaso(request):
    return render (request,'tablero_sextopaso.html')
