from django.contrib import admin
from django import forms
from .models import HistorialMedico, Mascota, CustomUser
from .forms import CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm
from .models import CustomUser
from .models import Cita

class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'edad', 'sexo', 'user')
    
    # Filtros laterales (sidebar)
    list_filter = ('especie', 'sexo')  # Filtra por especie y sexo
    
    # Búsqueda por nombre y raza
    search_fields = ('nombre', 'raza')
    
    # Si quieres agrupar por usuario en el admin
    list_select_related = ('user',)

    class Media:
        css = {
            'all': ('admin/css/custom_search_button.css',),
        }


# Filtro personalizado para Mascota (por especie o dueño)
class MascotaEspecieFilter(admin.SimpleListFilter):
    title = 'Especie de la mascota'
    parameter_name = 'especie'

    def lookups(self, request, model_admin):
        return Mascota.Especie.choices  # Usa las opciones del modelo Mascota

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(mascota__especie=self.value())

class HistorialMedicoAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista
    list_display = (
        'mascota',
        'mascota__sexo',       # Filtra por sexo de la mascota
        'vacuna_rabia',        # Filtra por vacunas (sí/no)
        'vacuna_moquillo',
        'desparasitacion_interna',
        'desparasitacion_externa',
        'ultima_consulta',     # Filtro por fecha
    )

    # Filtros laterales (sidebar)
    list_filter = (
        MascotaEspecieFilter,  # Filtro personalizado por especie
        'mascota__sexo',       # Filtra por sexo de la mascota
        'vacuna_rabia',        # Filtra por vacunas (sí/no)
        'vacuna_moquillo',
        'desparasitacion_interna',
        'desparasitacion_externa',
        'ultima_consulta',     # Filtro por fecha
    )

    # Búsqueda por nombre de mascota o dueño
    search_fields = (
        'mascota__nombre',     # Buscar por nombre de mascota
        'mascota__user__username',  # Buscar por dueño
    )

    # Ordenar por fecha descendente (más reciente primero)
    ordering = ('-ultima_consulta',)

# Registrar el modelo Mascota y CustomUser
admin.site.register(Mascota, MascotaAdmin)
admin.site.register(HistorialMedico, HistorialMedicoAdmin)
admin.site.register(CustomUser)


if admin.site.is_registered(CustomUser):
    admin.site.unregister(CustomUser)
    
class CustomUserChangeForm(UserChangeForm):
    password_readonly = forms.CharField(
        label="Contraseña",
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'readonly': 'readonly',
            'style': 'background-color: #f8f9fa; cursor: not-allowed;'
        })
    )

    class Meta(UserChangeForm.Meta):
        model = CustomUser
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            # Muestra los primeros caracteres del hash
            self.initial['password_readonly'] = self.instance.password[:30] + "..."
            # Elimina el campo password original para que no sea editable
            del self.fields['password']

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    list_display = ('username', 'first_name', 'last_name', 'is_staff')
    
    fieldsets = (
        (None, {'fields': ('username', 'password_readonly')}),
        ('Información personal', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Fechas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if obj:  # Solo para edición
            form.base_fields['password_readonly'].help_text = "Hash de contraseña (solo visualización)"
            if 'username' in form.base_fields:
                form.base_fields['username'].validators = []
                form.base_fields['username'].help_text = ''
        return form

admin.site.register(CustomUser, CustomUserAdmin)


@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('servicio_nombre', 'mascota_nombre', 'fecha', 'hora', 'usuario')
    list_filter = ('servicio', 'fecha')

    def servicio_nombre(self, obj):
        return obj.get_servicio_display()
    servicio_nombre.short_description = 'Servicio'

    def mascota_nombre(self, obj):
        return obj.mascota.nombre
    mascota_nombre.short_description = 'Mascota'
