from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
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

@login_required
def presentacion_interactiva(request):
    return render(request, 'presentacion_interactiva.html')

@login_required
def update_progress(request):
    if request.method == 'POST':
        clicks = int(request.POST.get('clicks', 0))
        user_profile = request.user.profile
        
        # Verificar si el progreso ya es 100%
        if user_profile.progreso >= 100:
            return JsonResponse({'progress': user_profile.progreso, 'message': 'Progreso completo, no se puede modificar más.'})
        
        # Solo actualizar si el progreso es menor a 100%
        if clicks <= 6:
            progress_percentage = (clicks / 6) * 100
            if progress_percentage > 100:
                progress_percentage = 100
            user_profile.progreso = progress_percentage
            user_profile.save()
            return JsonResponse({'progress': progress_percentage})
    return JsonResponse({'error': 'Invalid request'}, status=400)