from django.contrib import admin
from django.urls import path
from paciente.views import Index, NuevoSignosVitales, SignosVitalesView, clinica, domicilio, nuevoPaciente, pacienteinicio, editarPaciente, eliminarPaciente, historial, NuevoMedico, NuevoHistorial
from usuario.views import Login, logoutUser
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',login_required(pacienteinicio),name = 'index'),
    path('',login_required(Index.as_view()),name = 'index'),
    path('historial/<str:rut>/', historial, name = 'historial_clinico'),
    path('clinica/', login_required(clinica) , name= 'clinica'),
    path('domicilio/', login_required(domicilio), name= 'domicilio'),
    path('paciente/nuevo',nuevoPaciente, name='nuevoPaciente'),
    path('medico/nuevo', NuevoMedico.as_view(), name='nuevoMedico'),
    path('historialForm/nuevo', NuevoHistorial.as_view(), name='nuevoHistorial'),
    path('editarpaciente/<str:rut>/', login_required(editarPaciente), name='editarpaciente'),
    path('eliminarpaciente/<str:rut>/',login_required(eliminarPaciente), name='eliminarpaciente'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUser), name='logout'),
    path('paciente/SignosVitales', SignosVitalesView.as_view(), name='signosVitales'),
    path('paciente/NuevoSignosVitales', NuevoSignosVitales.as_view(), name='signosVtalesForm'),
]
