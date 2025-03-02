from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required
def septimopaso(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_tablerosextopaso < 100 
    ):
        return redirect('/sextopaso')  # Redirige de nuevo si no ha completado todo
    return render (request,'septimopaso.html')

@login_required
def frase_septimopaso(request):
    profile = request.user.profile
    profile.progreso_fraseseptimopaso = 100
    profile.save()
    return render (request,'frase_septimopaso.html')

@login_required
def imagen_septimopaso(request):
    profile = request.user.profile
    profile.progreso_imagenseptimopaso = 100
    profile.save()
    return render (request,'imagen_septimopaso.html')

def mi_plan_s2(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_fraseseptimopaso < 100 or
        profile.progreso_imagenseptimopaso < 100 or
        profile.progreso_imagen2septimopaso < 100 or
        profile.progreso_formatoseptimopaso < 100 
    ):
        return redirect('/septimopaso')
    return render (request,'mi_plan_s2.html')

@login_required
def infografia_septimopaso(request):
    return render (request,'infografia_septimopaso.html')

@login_required
def imagen2_septimopaso(request):
    profile = request.user.profile
    profile.progreso_imagen2septimopaso = 100
    profile.save()
    return render (request,'imagen2_septimopaso.html')

@login_required
def formato_septimopaso(request):
    profile = request.user.profile
    profile.progreso_formatoseptimopaso = 100
    profile.save()
    return render (request,'formato_septimopaso.html')

@login_required
def formato2_septimopaso(request):
    return render (request,'formato2_septimopaso.html')

