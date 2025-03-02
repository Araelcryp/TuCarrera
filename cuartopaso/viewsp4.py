from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
def cuartopaso(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_tablerotercerpaso < 100 or
        profile.progreso_videotercerpaso < 100 or
        profile.progreso_videoconsejotercerpaso < 100 or
        profile.progreso_presentaciontercerpaso < 100 
    ):
        return redirect('/mi-entorno-s2')  # Redirige de nuevo si no ha completado todo
    return render (request,'cuartopaso.html')

@login_required
def tablero_cuartopaso(request):
    return render (request,'tablero_cuartopaso.html')

@login_required
def video_cuartopaso(request):
    return render (request,'video_cuartopaso.html')

@login_required
def agenda_cuartopaso(request):
    return render (request,'agenda_cuartopaso.html')
