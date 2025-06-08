from django.contrib import admin
from django.urls import path
from mi_app import views  # Importa el módulo completo de views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='index'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('servicios/', views.servicios, name='servicios'),
    path('adopta/', views.adopta, name='adopta'),
    path('servicios/ayudas/', views.ayudas, name='ayudas'),
    path('servicios/cirugia/', views.cirugia, name='cirugia'),
    path('servicios/consulta/', views.consulta, name='consulta'),
    path('servicios/hospitalizacion/', views.hospitalizacion, name='hospitalizacion'),
    path('servicios/laboratorio/', views.laboratorio, name='laboratorio'),
    path('servicios/medicina/', views.medicina, name='medicina'),
    path('servicios/tramites/', views.tramites, name='tramites'),
    path('servicios/urgencias/', views.urgencias, name='urgencias'),
    path('signup/', views.signup, name='signup'),
    path('accounts/login/', RedirectView.as_view(url='/signin/', permanent=True)),
    path('citas/', views.citas, name='citas'),
    path('header/', views.header, name='header'),
    path('logout/', views.cerrarsesion, name='logout'),
    path('perfil/', views.perfil, name='perfil'),
    path('signin/', views.signin, name='signin'),
    path('crear_mascota/', views.crear_mascota, name='crear_mascota'),
    path('mascota/<int:mascota_id>/', views.mascota_detail, name='mascota_detail'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('blog/salud_felina/', views.salud_felina, name='salud_felina'),
    path('blog/enfermedades_perros/', views.enfermedades_perros, name='enfermedades_perros'),
    path('blog/vacunacion_gatos/', views.vacunacion_gatos, name='vacunacion_gatos'),
    path('blog/cuidado_perros/', views.cuidado_perros, name='cuidado_perros'),
    path('agendar_cita/', views.agendar_cita, name='agendar_cita'),
    path('enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),
    path('api/crear_cita/', views.crear_cita, name='crear_cita'),
    path('lista_citas/', views.lista_citas, name='lista_citas'),
]