from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required, user_passes_test

from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                user = User.objects.create_user(
                    username=request.POST['email'],
                    password=request.POST['password1']
                )
                user.email = request.POST['email']
                user.save()

                # Create user profile
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
                    "error": 'Email Already Exist'
                })
        return render(request, 'signup.html', {
            "error": 'Passwords do not match'
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
                'error': 'Username or Password is Incorrect'
            })
        else:
            login(request, user)
            return redirect('homeuser')
        
@login_required
def final(request):
    return render(request, 'final.html')