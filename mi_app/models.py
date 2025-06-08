from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

class CustomUser(AbstractUser):
    pass

    def __str__(self):
        return self.username
    
class Mascota(models.Model):
    
    class Especie(models.TextChoices):
        PERRO = 'Perro', 'Perro'
        GATO = 'Gato', 'Gato'
    
    class Sexo(models.TextChoices):
        MACHO = 'Macho', 'Macho'
        HEMBRA = 'Hembra', 'Hembra'
    
    nombre = models.CharField(max_length=100)
    especie = models.CharField(
        max_length=10,
        choices=Especie.choices,
        default=Especie.PERRO
    )
    raza = models.CharField(max_length=100)
    edad = models.PositiveIntegerField()
    sexo = models.CharField(
        max_length=10,
        choices=Sexo.choices,
        default=Sexo.MACHO
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='mascotas')

    def __str__(self):
        return f"{self.nombre} (Dueñ@: {self.user.username})"


class HistorialMedico(models.Model):
    mascota = models.ForeignKey('Mascota', on_delete=models.CASCADE)

    ultima_consulta = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=True, default=0.00)

    # Estas líneas se separarán con saltos de línea (\n), no con comas
    alergias = models.TextField(
        blank=True,
        help_text="Escribe una alergia por línea"
    )
    cirugias_previas = models.TextField(
        blank=True,
        help_text="Escribe una cirugía por línea"
    )
    enfermedades_cronicas = models.TextField(
        blank=True,
        help_text="Escribe una enfermedad por línea"
    )

    alimentacion = models.CharField(max_length=100, blank=True)
    hidratacion = models.CharField(max_length=100, blank=True)

    vacuna_moquillo = models.BooleanField(default=False)
    vacuna_parvovirus = models.BooleanField(default=False)
    vacuna_rabia = models.BooleanField(default=False)
    vacuna_leptospirosis = models.BooleanField(default=False)
    vacuna_polivalente = models.BooleanField(default=False)

    desparasitacion_interna = models.BooleanField(default=False)
    desparasitacion_externa = models.BooleanField(default=False)

    def __str__(self):
        return f"Historial de {self.mascota.nombre} (Dueñ@: {self.mascota.user.username})"
    
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _

class Cita(models.Model):
    class Servicio(models.TextChoices):
        CONSULTA_VETERINARIA = 'CV', _('Consulta Veterinaria')
        BANIO_Y_PELUQUERIA = 'BP', _('Baño y peluquería')
        VACUNACION = 'VA', _('Vacunación')
        TELEMEDICINA = 'TV', _('Telemedicina')
        TRAMITES_VIAJE = 'TVJ', _('Trámites de viaje')
        OTRO_SERVICIO = 'OT', _('Otro servicio')

    servicio = models.CharField(
        max_length=3,
        choices=Servicio.choices,
        default=Servicio.CONSULTA_VETERINARIA,
        verbose_name=_('Tipo de servicio')
    )
    fecha = models.DateField(verbose_name=_('Fecha'))
    hora = models.TimeField(verbose_name=_('Hora'))
    notas = models.TextField(blank=True, null=True, verbose_name=_('Notas adicionales'))
    creado_en = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))

    mascota = models.ForeignKey(
        'Mascota',  # Nombre exacto del modelo relacionado
        on_delete=models.CASCADE,
        verbose_name='Mascota',  # Añade esto
        related_name='citas'      # Añade esto
    )

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='citas_usuario',
        verbose_name=_('Usuario')
    )

    class Meta:
        verbose_name = _('Cita')
        verbose_name_plural = _('Citas')
        ordering = ['-fecha', '-hora']
        permissions = [
            ('puede_agendar_cita', _('Puede agendar citas')),
        ]

    def __str__(self):
        return f"{self.get_servicio_display()} - {self.mascota.nombre} ({self.fecha} {self.hora.strftime('%H:%M')})"