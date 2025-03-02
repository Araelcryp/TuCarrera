from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TestResult
from django.http import JsonResponse


@login_required
def segundopaso(request):
    profile = request.user.profile
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_testInteligencias < 100 or
        profile.progreso_inteligencias < 100 
    ):
        return redirect('/mis-intereses-s2')  # Redirige de nuevo si no ha completado todo
    
    return render (request,'segundopaso.html')


@login_required
def presentacion_segundopaso(request):
    profile = request.user.profile
    profile.progreso_presentacionsegundopaso = 100
    profile.save()
    return render (request,'presentacion_segundopaso.html')

@login_required
def instrucciones_segundopaso(request):
    profile = request.user.profile
    profile.progreso_testsegundopaso = 100
    profile.save()
    
    # Verificar si el usuario tiene resultados guardados
    test_completed = TestResult.objects.filter(user=request.user).exists()
    
    return render(request, "instrucciones_segundopaso.html", {"test_completed": test_completed})

@login_required
def test_segundopaso(request):
    return render (request,'test_segundopaso.html')

@login_required
def save_results(request):
    if request.method == "POST":
        user = request.user
        category = request.POST.get("category")
        score = request.POST.get("score")

        if category and score:
            result = TestResult(user=user, category=category, score=int(score))
            result.save()
            return JsonResponse({"message": f"Resultado guardado: {category} ({score})"}, status=200)
        else:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

CATEGORY_DESCRIPTIONS = {
    "rojo": "ÁREA PROFESIONAL: CIENCIAS SOCIALES - CARRERAS EN ADMINISTRACIÓN Y NEGOCIOS",
    "morado": "ÁREA PROFESIONAL: CIENCIAS FÍSICAS Y MATEMÁTICAS - CARRERAS EN INGENIERÍA Y MANUFACTURA",
    "azul": "ÁREA PROFESIONAL: CIENCIAS FÍSICAS Y MATEMÁTICAS - CARRERAS EN TECNOLOGÍAS DE LA INFORMACIÓN",
    "verde": "ÁREA PROFESIONAL: HUMANIDADES Y ARTES - CARRERAS EN HUMANIDADES Y ARTES",
    "amarillo": "ÁREA PROFESIONAL: CIENCIAS BIOLÓGICAS, QUÍMICAS Y DE LA SALUD - CARRERAS EN CIENCIAS DE LA SALUD",
    "gris": "ÁREA PROFESIONAL: CIENCIAS FÍSICAS Y MATEMÁTICAS - CARRERAS EN CIENCIAS NATURALES, MATEMÁTICA Y ESTADÍSTICA",
    "menta": "ÁREA PROFESIONAL: ARTES Y HUMANIDADES - CARRERAS EN EDUCACIÓN"
}

@login_required
def resultados_segundopaso(request):
    # Obtener el resultado más alto del usuario
    best_result = TestResult.objects.filter(user=request.user).order_by('-score').first()

    if best_result:
        best_result.description = CATEGORY_DESCRIPTIONS.get(best_result.category, "No se ha podido determinar una categoría.")

    return render(request, "resultados_segundopaso.html", {"result": best_result})