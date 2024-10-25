from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test

import re
from django.core.exceptions import ValidationError

from .models import Profile

# Create your views here.

def validate_password_strength(password):
    if len(password) < 8:
        raise ValidationError('La contraseña debe tener al menos 8 caracteres.')
    if not re.search(r'[A-Z]', password):
        raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')
    if not re.search(r'[a-z]', password):
        raise ValidationError('La contraseña debe contener al menos una letra minúscula.')
    if not re.search(r'[0-9]', password):
        raise ValidationError('La contraseña debe contener al menos un número.')
    if not re.search(r'[@$!%*?#]', password):
        raise ValidationError('La contraseña debe contener al menos un signo especial.')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return render(request, 'signup.html', {
                "error": 'Las contraseñas no coinciden.'
            })

        # Validar la fortaleza de la contraseña
        try:
            validate_password_strength(password1)
        except ValidationError as e:
            return render(request, 'signup.html', {
                "error": e.message
            })

        # Registrar usuario
        try:
            user = User.objects.create_user(
                username=request.POST['email'],
                password=password1
            )
            user.email = request.POST['email']
            user.save()

            # Crear perfil de usuario
            profile = Profile(
                user=user,
                apellido_paterno=request.POST['apellidoPaterno'],
                apellido_materno=request.POST['apellidoMaterno'],
                nombres=request.POST['nombres'],
                fecha_nacimiento=request.POST['fechaNacimiento'],
                curp=request.POST['curp'],
                procedencia=request.POST['procedencia'],  # 'si' o 'no'
                estado=request.POST.get('estado', None),  # Solo si la preparatoria es fuera de Querétaro
                institucion=request.POST.get('institucion', None),  # Solo si la preparatoria es fuera de Querétaro
                municipio=request.POST.get('municipio', None),  # Si la preparatoria es en Querétaro
                bachillerato=request.POST.get('bachillerato', None),  # Incluir opción de "otro"
                otro_bachillerato=request.POST.get('otro_bachillerato', None),  # Campo opcional si elige "otro"
                matricula=request.POST['matricula'],
                telefono=request.POST['telefono']
            )
            profile.save()
            login(request, user)
            return redirect('homeuser')
        except IntegrityError:
            return render(request, 'signup.html', {
                "error": 'El email ya existe.'
            })

@login_required
def homeuser(request):
    profile = request.user.profile  # Asumiendo que el perfil está relacionado con el usuario
    context = {
        'profile': profile
    }
    return render(request, 'homeuser.html', context)

@user_passes_test(lambda u: u.is_superuser, login_url='/permission-denied/')
def homeadmin(request):
    return render(request, 'homeadmin.html')

def permissiondenied(request):
    return render(request, 'permissiondenied.html')

def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html')
    else:
        user = authenticate(
            request, username=request.POST['email'], password=request.POST
            ['password'])
        if user is None:
            return render(request,'signin.html',{
                'error': 'Email o Contraseña Incorrectos'
            })
        else:
            login(request, user)
            return redirect('homeuser')
        
@login_required
def final(request):
    return render(request, 'final.html')