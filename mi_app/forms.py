from django import forms
from django.forms import ModelForm, ValidationError, inlineformset_factory
from .models import Mascota, HistorialMedico
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # Usa tu modelo personalizado



class CustomUserCreationForm(UserCreationForm):
    username = forms.EmailField(
        label='Correo electrónico',
        required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        label='Nombre',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        label='Apellido',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data.get('username').lower()
        if CustomUser.objects.filter(username=username).exists():
            raise ValidationError("Este correo electrónico ya está registrado")
        return username

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = user.username  # El correo se guarda también en el campo email
        if commit:
            user.save()
        return user
    
class MascotaForm(ModelForm):
    class Meta:
        model = Mascota
        fields = ['nombre', 'especie', 'raza', 'edad', 'sexo']

class HistorialMedicoForm(ModelForm):
    class Meta:
        model = HistorialMedico
        fields = [
            'mascota',
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
            'desparasitacion_externa',
        ]

        widgets = {
            'ultima_consulta': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control'
            }),
            'peso': forms.NumberInput(attrs={
                'step': '0.01',
                'class': 'form-control'
            }),
            'alergias': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Ej:\nPolen\nPolvo\nAlimentos específicos...',
                'class': 'form-control'
            }),
            'cirugias_previas': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Ej:\nEsterilización\nCirugía de fractura...',
                'class': 'form-control'
            }),
            'enfermedades_cronicas': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Ej:\nDiabetes\nInsuficiencia renal...',
                'class': 'form-control'
            }),
            'alimentacion': forms.TextInput(attrs={
                'placeholder': 'Ej: Concentrado, comida casera...',
                'class': 'form-control'
            }),
            'hidratacion': forms.TextInput(attrs={
                'placeholder': 'Ej: Agua limpia disponible, poco consumo...',
                'class': 'form-control'
            }),
        }

        labels = {
            'mascota': 'Mascota',
            'ultima_consulta': 'Última consulta',
            'peso': 'Peso (kg)',
            'alergias': 'Alergias (una por línea)',
            'cirugias_previas': 'Cirugías previas (una por línea)',
            'enfermedades_cronicas': 'Enfermedades crónicas (una por línea)',
            'alimentacion': 'Alimentación',
            'hidratacion': 'Hidratación',
            'vacuna_moquillo': 'Vacuna Moquillo',
            'vacuna_parvovirus': 'Vacuna Parvovirus',
            'vacuna_rabia': 'Vacuna Rabia',
            'vacuna_leptospirosis': 'Vacuna Leptospirosis',
            'vacuna_polivalente': 'Vacuna Polivalente',
            'desparasitacion_interna': 'Desparasitación Interna',
            'desparasitacion_externa': 'Desparasitación Externa',
        }
# Aquí agregamos el FormSet necesario
HistorialFormSet = inlineformset_factory(
    Mascota,
    HistorialMedico,
    form=HistorialMedicoForm,
    extra=1,
    can_delete=False
)