from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TestResult
from django.http import JsonResponse

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
def segundopaso(request):
    profile = request.user.profile
    
    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_inteligencias < 100 or
        profile.progreso_testInteligencias < 100 
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
    # Verificar si el usuario tiene resultados guardados
    test_completed = TestResult.objects.filter(user=request.user).exists()
    
    return render(request, "instrucciones_segundopaso.html", {"test_completed": test_completed})

@login_required
def test_segundopaso(request):
    profile = request.user.profile
    profile.progreso_testsegundopaso = 100
    profile.save()
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

            description = CATEGORY_DESCRIPTIONS.get(category, "Categoría desconocida")

            return JsonResponse({
                "category": category,
                "description": description,
                "score": score
            }, status=200)
        else:
            return JsonResponse({"error": "Datos incompletos"}, status=400)
    return JsonResponse({"error": "Método no permitido"}, status=405)

@login_required
def resultados_segundo_paso(request):
    best_result = TestResult.objects.filter(user=request.user).order_by('-score').first()

    context = {
        "result": {
            "category": best_result.category if best_result else None,
            "description": CATEGORY_DESCRIPTIONS.get(best_result.category, "No se ha podido determinar una categoría.") if best_result else None,
            "score": best_result.score if best_result else None
        } if best_result else None
    }

    return render(request, "resultados_segundopaso.html", context)