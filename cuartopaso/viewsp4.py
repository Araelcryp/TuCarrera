from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

# Create your views here.

@login_required
def cuartopaso(request):
    return render (request,'cuartopaso.html')

@login_required
def mi_universidad_s2(request):
    return render (request,'mi_universidad_s2.html')

@login_required
def mi_universidad_s3(request):
    return render (request,'mi_universidad_s3.html')

@login_required
def tablero_cuartopaso(request):
    return render (request,'tablero_cuartopaso.html')

@login_required
def video_cuartopaso(request):
    return render (request,'video_cuartopaso.html')

@login_required
def agenda_cuartopaso(request):
    return render (request,'agenda_cuartopaso.html')
