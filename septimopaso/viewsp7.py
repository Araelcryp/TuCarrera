from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required
def septimopaso(request):
    return render (request,'septimopaso.html')

@login_required
def frase_septimopaso(request):
    return render (request,'frase_septimopaso.html')

@login_required
def imagen_septimopaso(request):
    return render (request,'imagen_septimopaso.html')

@login_required
def video_septimopaso(request):
    return render (request,'video_septimopaso.html')

def mi_plan_s2(request):
    return render (request,'mi_plan_s2.html')

@login_required
def infografia_septimopaso(request):
    return render (request,'infografia_septimopaso.html')

@login_required
def imagen2_septimopaso(request):
    return render (request,'imagen2_septimopaso.html')

@login_required
def formato_septimopaso(request):
    return render (request,'formato_septimopaso.html')
