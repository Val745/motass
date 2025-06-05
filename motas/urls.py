from django.contrib import admin
from django.urls import path
from mi_app.views import index, header, mascota_detail, signin, perfil, crear_mascota, cerrarsesion, nosotros, servicios, adopta, ayudas, cirugia, consulta, hospitalizacion, laboratorio, medicina, tramites, urgencias, signup, citas, salud_felina, enfermedades_perros, vacunacion_gatos, cuidado_perros  # Importamos las vistas
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Ruta para la página principal
    path('index/', index, name='index'),  # Ruta para la página principal
    path('nosotros/', nosotros, name='nosotros'),
    path('servicios/', servicios, name='servicios'),
    path('adopta/', adopta, name='adopta'),
    path('servicios/ayudas/', ayudas, name='ayudas'),
    path('servicios/cirugia/', cirugia, name='cirugia'),
    path('servicios/consulta/', consulta, name='consulta'),
    path('servicios/hospitalizacion/', hospitalizacion, name='hospitalizacion'),
    path('servicios/laboratorio/', laboratorio, name='laboratorio'),
    path('servicios/medicina/', medicina, name='medicina'),
    path('servicios/tramites/', tramites, name='tramites'),
    path('servicios/urgencias/', urgencias, name='urgencias'),
    path('signup/', signup, name='signup'),
    path('accounts/login/', RedirectView.as_view(url='/signin/', permanent=True)),
    path('citas/', citas, name='citas'),
    path('header/', header, name='header'),
    path('logout/', cerrarsesion, name='logout'),
    path('perfil/', perfil, name='perfil'),
    path('signin/', signin, name='signin'),
    path('crear_mascota/', crear_mascota, name='crear_mascota'),
    path('mascota/<int:mascota_id>/', mascota_detail, name='mascota_detail'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('blog/salud_felina/', salud_felina, name='salud_felina'),
    path('blog/enfermedades_perros/', enfermedades_perros, name='enfermedades_perros'),
    path('blog/vacunacion_gatos/', vacunacion_gatos, name='vacunacion_gatos'),
    path('blog/cuidado_perros/', cuidado_perros, name='cuidado_perros'),
    path('agendar_cita/', views.agendar_cita, name='agendar_cita'),

]

