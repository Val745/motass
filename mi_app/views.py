from django.contrib import messages as django_messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import HistorialMedico, Mascota
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import HistorialFormSet, MascotaForm
import logging
from .models import Mascota, HistorialMedico
from .forms import MascotaForm, HistorialFormSet
from .forms import CitaForm

def index(request):
    return render(request, 'index.html')


def signup(request):
    try:
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                django_messages.success(request, '¡Registro exitoso!')
                return redirect('perfil')
            # Si el formulario no es válido, los errores estarán en form.errors
        else:
            form = CustomUserCreationForm()
        
        return render(request, 'signup.html', {'form': form})  # Elimina la variable 'error'
    except Exception as e:
        logging.exception("Error en el registro de usuario")
        raise
def perfil(request):
    mascotas = Mascota.objects.filter(user=request.user)
    return render(request, 'perfil.html', {'mascotas' : mascotas})


def cerrarsesion(request):
    logout(request)
    return redirect('index')


def signin(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)  # Usa el formulario de autenticación
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('perfil')
        # Si el formulario no es válido, se renderiza con errores
    else:
        form = AuthenticationForm()  # Formulario vacío para GET
    
    return render(request, 'signin.html', {'form': form})  # Pasa el formulario al contexto


def header(request):
    return render(request, 'header.html')

def crear_mascota(request):
    if request.method == 'GET':
        return render(request, 'crear_mascota.html',{
            'form': MascotaForm
        })
    else:
        try:
            form = MascotaForm(request.POST)
            new_mascota = form.save(commit=False)
            new_mascota.user = request.user
            new_mascota.save()
            return redirect('perfil')
        except ValueError:
            return render(request, 'crear_mascota.html', {
                'form': MascotaForm,
                'error': 'Por favor rellene los campos con datos validos'
            })

def nosotros(request):
    return render(request, 'nosotros.html')

def mascota_detail(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)

    # Solo crear HistorialMedico si NO existe y además es POST con datos válidos
    try:
        historial = HistorialMedico.objects.get(mascota=mascota)
    except HistorialMedico.DoesNotExist:
        historial = None

    form = MascotaForm(request.POST or None, instance=mascota)
    formset = HistorialFormSet(request.POST or None, instance=mascota)

    if request.method == 'POST':
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('mascota_detail', mascota_id=mascota.id)

    return render(request, 'mascota_detail.html', {
        'form': form,
        'formset': formset,
        'mascota': mascota,
        'historial': historial,
    })


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

def enfermedades_perros(request):
    return render(request, 'blog/enfermedades_perros.html')

def salud_felina(request):
    return render(request, 'blog/salud_felina.html')

def cuidado_perros(request):
    return render(request, 'blog/cuidado_perros.html')

def vacunacion_gatos(request):
    return render(request, 'blog/vacunacion_gatos.html')

def agendar_cita(request):
    if not request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = CitaForm(request.POST, user=request.user)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user
            cita.save()
            return redirect('perfil')  # O donde quieras redirigir
    else:
        form = CitaForm(user=request.user)
    return render(request, 'citas.html', {'form': form})