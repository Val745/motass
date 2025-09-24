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
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cita
from mi_app.models import Mascota
import json
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
    return render(request, 'perfil.html', {
        'user': request.user,
        'mascotas': mascotas
    })


def cerrarsesion(request):
    logout(request)
    return redirect('index')


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/perfil/')
        # Si el formulario no es válido, se renderiza con errores
        # Agrega esto para mostrar errores:
        return render(request, 'signin.html', {'form': form})
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

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

from django.forms import modelformset_factory
from django.shortcuts import get_object_or_404, redirect, render
from .models import Mascota, HistorialMedico
from .forms import MascotaForm

def mascota_detail(request, mascota_id):
    mascota = get_object_or_404(Mascota, id=mascota_id)
    
    # Usar los campos REALES de tu modelo HistorialMedico
    HistorialFormSet = modelformset_factory(
        HistorialMedico,
        fields=(
            'ultima_consulta', 
            'peso', 
            'alergias', 
            'cirugias_previas', 
            'enfermedades_cronicas', 
            'alimentacion', 
            'hidratacion', 
            'vacuna_moquillo', 
            'vacuna_parvovirus', 
            'vacuna_rabia', 
            'vacuna_leptospirosis', 
            'vacuna_polivalente', 
            'desparasitacion_interna', 
            'desparasitacion_externa'
        ),
        extra=0,
        can_delete=True
    )
    
    if request.method == 'POST':
        form = MascotaForm(request.POST, instance=mascota)
        formset = HistorialFormSet(
            request.POST, 
            queryset=HistorialMedico.objects.filter(mascota=mascota)
        )
        
        if form.is_valid() and formset.is_valid():
            form.save()
            instances = formset.save(commit=False)
            for instance in instances:
                instance.mascota = mascota
                instance.save()
            for obj in formset.deleted_objects:
                obj.delete()
            return redirect('mascota_detail', mascota_id=mascota.id)
    else:
        form = MascotaForm(instance=mascota)
        formset = HistorialFormSet(
            queryset=HistorialMedico.objects.filter(mascota=mascota)
        )

    return render(request, 'mascota_detail.html', {
        'form': form,
        'formset': formset,
        'mascota': mascota,
    })


def citas(request):
    mascotas = Mascota.objects.filter(user=request.user) if request.user.is_authenticated else []
    return render(request, 'citas.html', {
        'mascotas': mascotas,
    })

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

from django.shortcuts import render, redirect
from .forms import CitaForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from .forms import CitaForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='signin')  # Esto reemplaza tu verificación manual de autenticación
def agendar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST, user=request.user)
        if form.is_valid():
            cita = form.save(commit=False)
            # Asegúrate que tu modelo Cita tenga un campo 'user' en lugar de 'usuario'
            cita.user = request.user  # Cambiado de 'usuario' a 'user' para consistencia
            cita.save()
            return redirect('perfil')
    else:
        form = CitaForm(user=request.user)
    
    # Agrega contexto adicional si es necesario
    context = {
        'form': form,
        'mascotas': request.user.mascotas.all() if hasattr(request.user, 'mascotas') else []
    }
    
    return render(request, 'citas.html', context)

def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        email = request.POST.get('email')
        asunto = request.POST.get('asunto', 'Sin asunto')
        mensaje = request.POST.get('mensaje', '')

        cuerpo = f"Nombre: {nombre}\nTeléfono: {telefono}\nEmail: {email}\nMensaje: {mensaje}"

        send_mail(
            asunto,
            cuerpo,
            settings.DEFAULT_FROM_EMAIL,
            ['whiledebugging@gmail.com'],
            fail_silently=False,
        )
        return render(request, 'mensaje_enviado.html')
    return redirect('index')

from django.shortcuts import render
from .models import Cita

def lista_citas(request):
    citas = Cita.objects.all()
    return render(request, 'lista_citas.html', {'citas': citas})


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Cita, Mascota
from django.contrib.auth.decorators import login_required

@csrf_exempt
@login_required
def crear_cita(request):
    if request.method == 'POST':
        try:
            # Obtener datos del formulario
            servicio = request.POST.get('servicio')
            mascota_id = request.POST.get('mascota')
            fecha = request.POST.get('fecha')
            hora = request.POST.get('hora')
            notas = request.POST.get('notas', '')
            
            # Validaciones básicas
            if not all([servicio, mascota_id, fecha, hora]):
                return JsonResponse({
                    'success': False, 
                    'error': 'Todos los campos obligatorios son requeridos'
                }, status=400)
            
            # Verificar que la mascota pertenece al usuario
            mascota = Mascota.objects.get(id=mascota_id, user=request.user)
            
            # Validar que no exista una cita para ese usuario en esa fecha y hora
            cita_existente = Cita.objects.filter(
                fecha=fecha,
                hora=hora
            ).exists()

            
            if cita_existente:
                return JsonResponse({
                    'success': False,
                    'error': 'Ese horario ya está ocupado, por favor elige otro'
                }, status=400)
            
            # Crear y guardar la cita
            cita = Cita.objects.create(
                usuario=request.user,
                mascota=mascota,
                servicio=servicio,
                fecha=fecha,
                hora=hora,
                notas=notas
            )
            
            return JsonResponse({
                'success': True,
                'cita_id': cita.id
            })
            
        except Mascota.DoesNotExist:
            return JsonResponse({
                'success': False, 
                'error': 'Mascota no encontrada o no pertenece al usuario'
            }, status=404)
            
        except Exception as e:
            return JsonResponse({
                'success': False, 
                'error': str(e)
            }, status=500)
    
    return JsonResponse({
        'success': False, 
        'error': 'Método no permitido'
    }, status=405)

