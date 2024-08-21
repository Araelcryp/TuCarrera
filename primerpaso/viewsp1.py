from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def primerpaso(request):
    return render (request,'primerpaso.html')

@login_required
def imagen_primerpaso(request):
    return render(request,'imagen_primerpaso.html')

@login_required
def presentacion_primerpaso(request):
    return render(request,'presentacion_primerpaso.html')

@login_required
def video_primerpaso(request):
    return render(request,'video_primerpaso.html')

@login_required
def formato_primerpaso(request):
    return render(request,'formato_primerpaso.html')

@login_required
def primerpasos2(request):
    return render(request,'mis_intereses_s2.html')

@login_required
def infografia_primerpaso(request):
    return render(request,'infografia_primerpaso.html')

@login_required
def instrucciones_primerpaso(request):
    return render(request,'instrucciones_primerpaso.html')

@login_required
def test_primerpaso(request):
    return render(request,'test_primerpaso.html')

@login_required
def resultados_primerpaso(request):
    return render(request,'resultados_primerpaso.html')