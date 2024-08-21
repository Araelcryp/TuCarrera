from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

@login_required
def sextopaso(request):
    return render (request,'sextopaso.html')

@login_required
def tablero_sextopaso(request):
    return render (request,'tablero_sextopaso.html')
