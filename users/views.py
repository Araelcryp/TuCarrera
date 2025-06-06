from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test

import re
from django.core.exceptions import ValidationError

from .forms import SignupForm
from .models import Profile, Meta

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from django.shortcuts import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os
from django.conf import settings
from django.http import HttpResponse
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.utils import ImageReader
from segundopaso.models import TestResult
from django.http import FileResponse, HttpResponse
from .models import Profile, Constancia
from django.core.mail import EmailMessage
from django.core.files.storage import default_storage
from django.contrib.staticfiles import finders

from django.http import JsonResponse
import json
from datetime import datetime
from django.utils import timezone

import csv
from django.http import StreamingHttpResponse


# Create your views here.

# def validate_password_strength(password):
#     if len(password) < 8:
#         raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
#     if not re.search(r'[A-Z]', password):
#         raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')
#     if not re.search(r'[a-z]', password):
#         raise ValidationError('La contraseña debe contener al menos una letra minúscula.')
#     if not re.search(r'[0-9]', password):
#         raise ValidationError('La contraseña debe contener al menos un número.')
#     if not re.search(r'[@$!%*?#]', password):
#         raise ValidationError('La contraseña debe contener al menos un signo especial.')

# def validate_curp(curp):
#     curp = curp.upper()
#     REGEX_CURP = r'^[A-ZÑ]{4}\d{6}[HM][A-Z]{5}\d[A-Z0-9]$'
#     if len(curp) != 18:
#         raise ValidationError('CURP inválida. Debe tener 18 caracteres.')
#     if not re.match(REGEX_CURP, curp):
#         raise ValidationError('CURP inválida. Verifica que tenga el formato correcto.')


def signup(request):
    if request.method == "GET":
        form = SignupForm()
        return render(request, "signup.html", {"form": form})
    else:
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                user = User.objects.create_user(
                    username=form.cleaned_data["email"],
                    password=form.cleaned_data["password1"],
                )
                user.save()

                # Crear perfil de usuario
                profile = Profile(
                    user=user,
                    apellido_paterno=form.cleaned_data["apellidoPaterno"],
                    apellido_materno=form.cleaned_data["apellidoMaterno"],
                    nombres=form.cleaned_data["nombres"],
                    fecha_nacimiento=form.cleaned_data["fechaNacimiento"],
                    curp=form.cleaned_data["curp"],
                    procedencia=request.POST["procedencia"],
                    estado=request.POST.get("estado", None),
                    institucion=request.POST.get("institucion", None),
                    municipio=request.POST.get("municipio", None),
                    bachillerato=request.POST.get("bachillerato", None),
                    otro_bachillerato=request.POST.get("otro_bachillerato", None),
                    matricula=request.POST.get("matricula", None),
                    telefono=form.cleaned_data["telefono"],
                    email_tutor=form.cleaned_data["email_tutor"],
                )
                profile.save()

                # Enviar correo de confirmación
                html_content = render_to_string(
                    "confirmation_email.html",
                    {
                        "nombre": profile.nombres,
                    },
                )
                text_content = strip_tags(html_content)
                send_mail(
                    "Confirmación de cuenta",
                    text_content,
                    "sedeq.coord@gmail.com",
                    [user.username],
                    html_message=html_content,
                    fail_silently=False,
                )

                login(request, user)
                return redirect("homeuser")
            except IntegrityError:
                form.add_error("email", "El email ya existe.")
        # Si hay errores, se re-renderiza el formulario con los datos válidos ya mantenidos
        return render(request, "signup.html", {"form": form})


@login_required
def update_profile(request):
    if request.method == "POST":
        user = request.user
        profile = user.profile

        email = request.POST.get("email")
        telefono = request.POST.get("telefono")
        password = request.POST.get("password")

        if email:
            user.email = email
            user.username = email  # Para mantener la coherencia con el login
            user.save()

        if telefono:
            profile.telefono = telefono
            profile.save()

        if password:
            user.set_password(password)
            user.save()

        return JsonResponse({"status": "success"})

    return JsonResponse(
        {"status": "error", "message": "Método no permitido"}, status=400
    )


@login_required
def homeuser(request):
    profile = request.user.profile

    # Si el usuario no ha ingresado el correo de su tutor, lo redirige a la vista correspondiente
    if not profile.email_tutor:
        return redirect("completar_tutor_email")

    context = {"profile": profile}
    return render(request, "homeuser.html", context)


@login_required
def completar_tutor_email(request):
    profile = request.user.profile

    if request.method == "POST":
        email_tutor = request.POST.get("email_tutor")
        if email_tutor:
            profile.email_tutor = email_tutor
            profile.save()
            return redirect(
                "homeuser"
            )  # Una vez completado, regresa a la página principal

    return render(request, "completar_tutor_email.html", {"profile": profile})


@user_passes_test(lambda u: u.is_superuser, login_url="/permission-denied/")
def homeadmin(request):
    return render(request, "homeadmin.html")


def permissiondenied(request):
    return render(request, "permissiondenied.html")


def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html")
    else:
        user = authenticate(
            request, username=request.POST["email"], password=request.POST["password"]
        )
        if user is None:
            return render(
                request, "signin.html", {"error": "Email o Contraseña Incorrectos"}
            )
        else:
            login(request, user)
            return redirect("homeuser")


CATEGORY_DESCRIPTIONS = {
    "rojo": "Ciencias sociales",
    "morado": "Ciencias físicas y matemáticas",
    "azul": "Ciencias físicas y matemáticas",
    "verde": "Humanidades y artes",
    "amarillo": "Ciencias biológicas, químicas y de la salud",
    "gris": "Ciencias físicas y matemáticas",
    "menta": "Artes y humanidades",
}


@login_required
def final(request):
    profile = request.user.profile

    # Verificar si todos los progresos están al 100%
    if (
        profile.progreso_infografiaseptimopaso < 100
        or profile.progreso_formato2septimopaso < 100
    ):
        return redirect("/mi-plan-s2")
    return render(request, "final.html")


"""Calcula el porcentaje de progreso basado en una lista de valores."""


def calcular_porcentaje(progresos):
    progresos = [p or 0 for p in progresos]  # Evitar valores None
    total_progreso = sum(progresos)
    progreso_maximo = len(progresos) * 100  # Cada sección tiene un máximo de 100%
    return (total_progreso / progreso_maximo) * 100 if progreso_maximo > 0 else 0


@login_required
def obtener_tiempo_plataforma(request):
    tiempo_en_plataforma = round(
        (timezone.now() - request.user.date_joined).total_seconds() / 3600, 1
    )
    return JsonResponse({"tiempo": tiempo_en_plataforma})


@login_required
def perfil(request):
    profile = request.user.profile

    tiempo_en_plataforma = round(
        (timezone.now() - request.user.date_joined).total_seconds() / 3600, 1
    )  # Convertir a horas

    # Definir distintas categorías de progreso
    progresos_p1 = [
        profile.progreso_personalidad,
        profile.progreso_autoestima,
        profile.progreso_valores,
        profile.progreso_logros,
        profile.progreso_inteligencias,
        profile.progreso_testInteligencias,
    ]

    progresos_p2 = [
        profile.progreso_presentacionsegundopaso,
        profile.progreso_testsegundopaso,
    ]

    progresos_p3 = [
        profile.progreso_presentacionsegundopaso,
        profile.progreso_testsegundopaso,
    ]

    progresos_p3 = [
        profile.progreso_infografiatercerpaso,
        profile.progreso_tablerotercerpaso,
        profile.progreso_videotercerpaso,
        profile.progreso_videoconsejotercerpaso,
        profile.progreso_presentaciontercerpaso,
    ]

    progresos_p4 = [
        profile.progreso_tablerocuartopaso,
        profile.progreso_videocuartopaso,
        profile.progreso_agendacuartopaso,
    ]

    progresos_p5 = [
        profile.progreso_imagenquintopaso,
        profile.progreso_tableroquintopaso,
        profile.progreso_infografiaquintopaso,
    ]

    progresos_p6 = [
        profile.progreso_tablerosextopaso,
    ]

    progresos_p7 = [
        profile.progreso_fraseseptimopaso,
        profile.progreso_imagenseptimopaso,
        profile.progreso_imagen2septimopaso,
        profile.progreso_formatoseptimopaso,
        profile.progreso_infografiaseptimopaso,
        profile.progreso_formato2septimopaso,
    ]

    # Calcular los porcentajes usando la función
    porcentaje_total_p1 = calcular_porcentaje(progresos_p1)
    porcentaje_total_p2 = calcular_porcentaje(progresos_p2)
    porcentaje_total_p3 = calcular_porcentaje(progresos_p3)
    porcentaje_total_p4 = calcular_porcentaje(progresos_p4)
    porcentaje_total_p5 = calcular_porcentaje(progresos_p5)
    porcentaje_total_p6 = calcular_porcentaje(progresos_p6)
    porcentaje_total_p7 = calcular_porcentaje(progresos_p7)

    context = {
        "profile": profile,
        "porcentaje_total_p1": porcentaje_total_p1,
        "porcentaje_total_p2": porcentaje_total_p2,
        "porcentaje_total_p3": porcentaje_total_p3,
        "porcentaje_total_p4": porcentaje_total_p4,
        "porcentaje_total_p5": porcentaje_total_p5,
        "porcentaje_total_p6": porcentaje_total_p6,
        "porcentaje_total_p7": porcentaje_total_p7,
        "tiempo_en_plataforma": tiempo_en_plataforma,
    }

    return render(
        request,
        "perfil.html",
        context,
    )


@login_required
def generar_constancia_pdf(request):
    usuario = request.user
    perfil = getattr(usuario, "profile", None)

    # Obtener el nombre del usuario
    nombre_completo = (
        f"{perfil.nombres} {perfil.apellido_paterno} {perfil.apellido_materno}"
        if perfil
        else usuario.get_full_name() or usuario.username
    )

    # Definir la carpeta de almacenamiento
    carpeta_bachillerato = (
        os.path.join(
            perfil.municipio or "Desconocido", perfil.bachillerato or "Sin_Bachillerato"
        )
        if perfil and perfil.procedencia == "si"
        else (
            os.path.join(
                perfil.estado or "Desconocido", perfil.institucion or "Sin_Institucion"
            )
            if perfil and perfil.procedencia == "no"
            else (
                os.path.join("Otras", perfil.otro_bachillerato)
                if perfil and perfil.otro_bachillerato
                else "Otras"
            )
        )
    ).replace(" ", "_")

    ruta_bachillerato = os.path.join(
        settings.MEDIA_ROOT, "constancias", carpeta_bachillerato
    )
    os.makedirs(ruta_bachillerato, exist_ok=True)

    # Nombre del archivo PDF
    nombre_pdf = f"Constancia_{''.join(e for e in nombre_completo if e.isalnum() or e in (' ', '_')).replace(' ', '_')}.pdf"
    ruta_pdf = os.path.join(ruta_bachillerato, nombre_pdf)

    # Crear el PDF
    p = canvas.Canvas(ruta_pdf, pagesize=(960, 720))
    # imagen_path = finders.find("images/constancia.png")
    # if not imagen_path:
    #
    #     return HttpResponse("No se encontró la imagen de la constancia", status=404)

    p.drawImage("./users/static/images/Constancia.png", 0, 0, width=960, height=720)

    # Obtener el resultado del test
    test_result = (
        TestResult.objects.filter(user=usuario).order_by("-date_taken").first()
    )
    resultado = (
        CATEGORY_DESCRIPTIONS.get(test_result.category, "Categoría desconocida")
        if test_result
        else "No disponible"
    )

    # Ajustar posición del texto según el resultado
    posiciones_x = {
        "rojo": 400,
        "morado": 325,
        "azul": 325,
        "verde": 380,
        "amarillo": 260,
        "gris": 325,
        "menta": 380,
    }
    resultado_x = posiciones_x.get(test_result.category, 315)

    # Dibujar textos en el PDF
    p.setFont("Helvetica-Bold", 24)
    p.setFillColorRGB(0.0, 0.2, 0.6)
    p.drawCentredString(1000 / 2, 375, f"A: {nombre_completo}")
    p.drawString(resultado_x, 190, resultado)
    p.showPage()
    p.save()

    # Guardar en la base de datos y verificar si ya se envió el correo
    constancia, created = Constancia.objects.update_or_create(
        user=usuario,
        bachillerato=perfil.bachillerato if perfil else "Otras",
        defaults={"archivo": f"constancias/{carpeta_bachillerato}/{nombre_pdf}"},
    )

    # Solo enviar el correo si la constancia aún no ha sido enviada
    if not constancia.enviado:
        enviar_constancia_por_correo(usuario, ruta_pdf)
        constancia.enviado = True
        constancia.save()

    return FileResponse(open(ruta_pdf, "rb"), content_type="application/pdf")


def enviar_constancia_por_correo(usuario, ruta_pdf):
    """Envía la constancia al correo del usuario y del tutor si está registrado."""
    perfil = getattr(usuario, "profile", None)

    # Obtener los correos de usuario y tutor
    destinatarios = [usuario.username]
    if perfil and perfil.email_tutor:
        destinatarios.append(perfil.email_tutor)

    # Si no hay correos, no se envía nada
    if not destinatarios:
        return

    asunto = "Tu constancia ha sido generada"
    mensaje = f"""
    Estimado/a {perfil.nombres},
    
    Nos complace informarle que su constancia ha sido generada y se adjunta a este correo en formato PDF.

    Encontrará en el documento adjunto los detalles de su finalización del curso.

    Le agradecemos su participación.

    Atentamente,
    El equipo de Contigo tu carrera universitaria.
    """

    email = EmailMessage(asunto, mensaje, settings.DEFAULT_FROM_EMAIL, destinatarios)

    # Adjuntar el PDF
    with default_storage.open(ruta_pdf, "rb") as pdf_file:
        email.attach("Constancia.pdf", pdf_file.read(), "application/pdf")

    email.send()


@login_required
def agregar_meta(request):
    if request.method == "POST":
        data = json.loads(request.body)
        descripcion = data.get("meta")
        fecha_objetivo_str = data.get("fecha")  # Esta es una cadena

        if not descripcion or not fecha_objetivo_str:
            return JsonResponse(
                {"status": "error", "message": "Todos los campos son obligatorios"},
                status=400,
            )

        try:
            fecha_objetivo = datetime.strptime(
                fecha_objetivo_str, "%Y-%m-%d"
            ).date()  # 👈 Convertir string a date
        except ValueError:
            return JsonResponse(
                {"status": "error", "message": "Formato de fecha inválido"}, status=400
            )

        nueva_meta = Meta.objects.create(
            user=request.user, descripcion=descripcion, fecha_objetivo=fecha_objetivo
        )

        return JsonResponse(
            {
                "status": "success",
                "meta": {
                    "id": nueva_meta.id,
                    "descripcion": nueva_meta.descripcion,
                    "fecha": nueva_meta.fecha_objetivo.strftime(
                        "%d-%m-%Y"
                    ),  # Ahora sí es un date
                    "completada": nueva_meta.completada,
                },
            }
        )

    return JsonResponse(
        {"status": "error", "message": "Método no permitido"}, status=400
    )


@login_required
def obtener_metas(request):
    metas = Meta.objects.filter(user=request.user).order_by("fecha_objetivo")
    metas_list = [
        {
            "id": meta.id,
            "descripcion": meta.descripcion,
            "fecha": meta.fecha_objetivo.strftime("%d-%m-%Y"),
            "completada": meta.completada,
        }
        for meta in metas
    ]

    return JsonResponse({"status": "success", "metas": metas_list})




# CSV Export
def es_admin(user):
    return user.is_active and user.is_superuser

class EchoBuffer:
    def write(self, value):
        return value

@user_passes_test(es_admin)
def export_signups_csv(request):
    """
    Genera un CSV con todos los registros de Signup.
    Solo se accede si el usuario es superuser.
    """
    pseudo_buffer = EchoBuffer()
    writer = csv.writer(pseudo_buffer)

    # 1) Fila de encabezados (ajusta los nombres a los de tu modelo)
    headers = [
        'username',           
        'apellido_paterno',
        'apellido_materno',
        'nombres',
        'fecha_nacimiento',
        'curp',
        'procedencia',
        'estado',
        'institucion',
        'municipio',
        'bachillerato',
        'otro_bachillerato',
        'matricula',
        'telefono',
        'email_tutor',
    ]

    def row_generator():
        # Escribimos primero la fila de encabezados
        yield writer.writerow(headers)
        # Recorremos todos los Signup (usa .iterator() para no cargar todo en memoria)
        for p in Profile.objects.select_related('user').iterator():
            yield writer.writerow([
                p.user.username,
                p.apellido_paterno,
                p.apellido_materno,
                p.nombres,
                p.fecha_nacimiento,
                p.curp,
                p.procedencia,
                p.estado or '',
                p.institucion or '',
                p.municipio or '',
                p.bachillerato or '',
                p.otro_bachillerato or '',
                p.matricula,
                p.telefono,
                p.email_tutor or '',
            ])

    response = StreamingHttpResponse(
        row_generator(),
        content_type='text/csv'
    )
    # Fuerza la descarga del archivo
    response['Content-Disposition'] = 'attachment; filename="signups.csv"'
    return response

