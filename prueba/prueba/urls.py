"""
URL configuration for prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inicio import views
from django.conf import settings
from registros import views as views_registros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name="Principal"),
    path('contacto/', views_registros.contacto, name="Contacto"),
    path('formulario/', views.formulario, name="Formulario"),
    path('seguridad/', views.seguridad, name="Seguridad"),
    path('registrar/', views_registros.registrar, name="Registrar"),
    path('comentarios/', views_registros.comentarios, name="Comentarios"),
    path('eliminarComentario/<int:id>/', views_registros.eliminarComentarioContacto, name="Eliminar"),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('consulta1', views_registros.consultar1, name="Consultas"),
    path('consulta2', views_registros.consultar2, name="Consultas2"),
    path('consulta3', views_registros.consultar3, name="Consultas3"),
    path('consulta4', views_registros.consultar4, name="Consultas4"),
    path('consulta5', views_registros.consultar5, name="Consultas5"),
    path('consulta6', views_registros.consultar6, name="Consultas6"),
    path('consulta7', views_registros.consultar7, name="Consultas7"),
    path('consulta8', views_registros.consultarSQL, name="Consultar8"),


]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)