from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TestResult
from django.http import JsonResponse


@login_required
def segundopaso(request):
    return render (request,'segundopaso.html')

@login_required
def frase_segundopaso(request):
    return render (request,'frase_segundopaso.html')

@login_required
def presentacion_segundopaso(request):
    return render (request,'presentacion_segundopaso.html')

@login_required
def instrucciones_segundopaso(request):
    return render (request,'instrucciones_segundopaso.html')

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
    results = TestResult.objects.filter(user=request.user).order_by('-date_taken')

    for result in results:
        result.description = CATEGORY_DESCRIPTIONS.get(result.category, "No se ha podido determinar una categoría.")

    return render(request, "resultados_segundopaso.html", {"results": results})