from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
def tercerpaso(request):
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