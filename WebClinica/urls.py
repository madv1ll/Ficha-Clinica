"""WebClinica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from paciente.views import clinica, domicilio, nuevoMedico, nuevoPaciente, pacienteinicio, editarPaciente, eliminarPaciente, historial
from usuario.views import Login, logoutUser
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',pacienteinicio,name = 'index'),
    path('historial/<str:rut>/', historial, name = 'historial_clinico'),
    path('clinica/', login_required(clinica) , name= 'clinica'),
    path('domicilio/', domicilio, name= 'domicilio'),
    path('paciente/nuevo',nuevoPaciente, name='nuevoPaciente'),
    path('medico/nuevo',nuevoMedico, name='nuevoMedico'),
    path('editarpaciente/<str:rut>/', editarPaciente, name='editarpaciente'),
    path('eliminarpaciente/<str:rut>/', eliminarPaciente, name='eliminarpaciente'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUser), name='logout'),
]
