from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Cliente  # Modelo basado en tu BD
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse


def index(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # register user
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('perfil')
            
            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'El usuario ya existe'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Contraseñas no coinciden'
        })

def perfil(request):
    return render(request, 'perfil.html')

def cerrarsesion(request):
    logout(request)
    return redirect('index.html')

def header(request):
    return render(request, 'header.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def citas(request):
    return render(request, 'citas.html')

def adopta(request):
    return render(request, 'adopta.html')


def servicios(request):
    return render(request, 'servicios.html')


def ayudas(request):
    # Asegúrate de que esta ruta coincide con la ubicación real
    return render(request, 'servicios/ayudas.html')


def cirugia(request):
    return render(request, 'servicios/cirugia.html')


def consulta(request):
    return render(request, 'servicios/consulta.html')


def hospitalizacion(request):
    return render(request, 'servicios/hospitalizacion.html')


def laboratorio(request):
    return render(request, 'servicios/laboratorio.html')


def medicina(request):
    return render(request, 'servicios/medicina.html')


def tramites(request):
    return render(request, 'servicios/tramites.html')


def urgencias(request):
    return render(request, 'servicios/urgencias.html')
