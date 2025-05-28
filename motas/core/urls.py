from django.contrib import admin
from django.urls import path
from mi_app.views import index, header, perfil, logout, nosotros, servicios, adopta, ayudas, cirugia, consulta, hospitalizacion, laboratorio, medicina, tramites, urgencias, signup, citas  # Importamos las vistas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),  # Ruta para la página principal
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
    path('servicios/urgencias/', urgencias, name='urgencias'),
    path('signup/', signup, name='signup'),
    path('citas/', citas, name='citas'),
    path('header/', header, name='header'),
    path('logout/', logout, name='logout'),
    path('perfil/', perfil, name='perfil'),


]

