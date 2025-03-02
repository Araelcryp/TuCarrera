import json
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import TestResult
# Create your views here.

@login_required
def primerpaso(request):
    return render (request,'primerpaso.html')

@login_required
def imagen_primerpaso(request):
    profile = request.user.profile
    profile.progreso_personalidad = 100
    profile.save()
    return render(request, 'imagen_primerpaso.html')

@login_required
def presentacion_primerpaso(request):
    profile = request.user.profile
    profile.progreso_autoestima = 100
    profile.save()
    return render(request, 'presentacion_primerpaso.html')

@login_required
def video_primerpaso(request):
    profile = request.user.profile
    profile.progreso_valores = 100
    profile.save()
    return render(request, 'video_primerpaso.html')

@login_required
def formato_primerpaso(request):
    profile = request.user.profile
    profile.progreso_logros = 100
    profile.save()
    return render(request, 'formato_primerpaso.html')

@login_required
def primerpasos2(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_personalidad < 100 or
        profile.progreso_autoestima < 100 or
        profile.progreso_valores < 100 or
        profile.progreso_logros < 100
    ):
        return redirect('/primerpaso')  # Redirige de nuevo si no ha completado todo
    
    return render(request, 'mis_intereses_s2.html')

@login_required
def infografia_primerpaso(request):
    profile = request.user.profile
    profile.progreso_inteligencias = 100
    profile.save()
    return render(request,'infografia_primerpaso.html')

@login_required
def instrucciones_primerpaso(request):
    try:
        resultado = TestResult.objects.get(user=request.user)
        completado = resultado.completado  # Obtener el estado de completado
    except TestResult.DoesNotExist:
        completado = False  # Si no hay registro, el test no está completado

    return render(request, "instrucciones_primerpaso.html", {"completado": completado})

@login_required
def test_primerpaso(request):
    profile = request.user.profile
    profile.progreso_testInteligencias = 100
    profile.save()
    return render(request,'test_primerpaso.html')

@login_required
def resultados_primer_paso(request):
    try:
        resultado = TestResult.objects.get(user=request.user)

        # Crear un diccionario con las inteligencias y sus puntajes
        inteligencias = {
            "📖 Inteligencia Verbal": resultado.inteligencia_verbal,
            "🔢 Inteligencia Lógica": resultado.inteligencia_logica,
            "🎨 Inteligencia Visual": resultado.inteligencia_visual,
            "🤸‍♂️ Inteligencia Corporal": resultado.inteligencia_corporal,
            "🎵 Inteligencia Musical": resultado.inteligencia_musical,
            "🧠 Inteligencia Intrapersonal": resultado.inteligencia_intrapersonal,
            "🤝 Inteligencia Interpersonal": resultado.inteligencia_interpersonal,
        }

        # Ordenar y seleccionar las 3 más altas
        top_3 = sorted(
            [(nombre, puntaje) for nombre, puntaje in inteligencias.items() if puntaje > 0],
            key=lambda x: x[1],
            reverse=True
        )[:3]  

    except TestResult.DoesNotExist:
        top_3 = None  

    return render(request, "resultados_primerpaso.html", {"top_3": top_3})

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

@login_required
def guardar_resultados(request):
    if request.method == "POST":
        data = json.loads(request.body)
        resultado, created = TestResult.objects.get_or_create(user=request.user)
        
        resultado.inteligencia_verbal = data.get('A', 0)
        resultado.inteligencia_logica = data.get('B', 0)
        resultado.inteligencia_visual = data.get('C', 0)
        resultado.inteligencia_corporal = data.get('D', 0)
        resultado.inteligencia_musical = data.get('E', 0)
        resultado.inteligencia_intrapersonal = data.get('F', 0)
        resultado.inteligencia_interpersonal = data.get('G', 0)
        resultado.completado = True
        resultado.save()

        return JsonResponse({"success": True})
    return JsonResponse({"error": "Método no permitido"}, status=405)