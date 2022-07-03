"""cursosDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from os import stat
from django.contrib import admin
from django.urls import path
from contenido import views
from cursos import views as views_cursos
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_cursos.principal, name="Principal"),
    path('cursos/', views.cursos, name="Cursos"),
    path('contacto/', views_cursos.contacto, name="Contacto"),
    path('registrar/', views_cursos.registrar, name="Registrar"),
    path('consultaCurso/', views_cursos.consultaCurso, name="consultaCurso"),
    path('registraCurso/', views_cursos.registraCurso, name="registraCurso"),
    path('formRegistroCurso/', views_cursos.formRegistroCurso, name="formRegistroCurso"),
    path('eliminarCurso/<int:id>/', views_cursos.eliminarCurso, name="eliminarCurso"),
    path('formEditarCurso/<int:id>/', views_cursos.consultaCursoIndividual, name="ConsultaIndividual"),
    path('editarComentario/<int:id>/', views_cursos.editaCurso, name="Editar"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)