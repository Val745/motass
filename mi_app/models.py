from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils import timezone

class CustomUser(AbstractUser):
    # Estos campos ya vienen en AbstractUser, así que no es necesario redefinirlos:
    # username, email, first_name, last_name, password, etc.

    # Puedes agregar más campos personalizados si quieres. Ejemplo:
    # telefono = models.CharField(max_length=15, blank=True, null=True)
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
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

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