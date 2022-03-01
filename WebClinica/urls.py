from django.contrib import admin
from django.urls import path
from paciente.views import Index,  NuevoSignosVitales, ReportePDF, SignosViews, evolucion, historialDetalle, nuevaEvolucion, nuevoHistorialf, nuevoPaciente, editarPaciente, eliminarPaciente, historial, NuevoMedico, nuevoSignosVitales, signosDetalle, signosVitales, editarHistorial, editarSignos, ReporteExcel
from usuario.views import Login, logoutUser
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login_required(Index.as_view()),name = 'index'),
    #Paciente CRUD
    path('paciente/nuevo',nuevoPaciente, name='nuevoPaciente'),
    path('editarpaciente/<str:rut>/', login_required(editarPaciente), name='editarpaciente'),
    path('eliminarpaciente/<str:rut>/',login_required(eliminarPaciente), name='eliminarpaciente'),
    #Historial Paciente
    path('historial/<str:rut>/', login_required(historial), name = 'historial_clinico'),
    path('historialForm/nuevo/<str:rut>', nuevoHistorialf, name='nuevoHistorial'),
    path('historial/historialdetalle/<str:id>', historialDetalle, name='historialdetalle'),
    path('historial/editarHistorial/<str:id>', editarHistorial, name='EditarHistorial'),
    #Cuentas
    path('medico/nuevo', NuevoMedico.as_view(), name='nuevoMedico'),
    path('accounts/login/', Login.as_view(), name='login'),
    path('logout/', login_required(logoutUser), name='logout'),
    #Signos Vitales
    path('SignosVitales/<str:rut>/', login_required(signosVitales), name='signosVitales'),
    path('SignosVitales/<str:rut>/NuevoSignosVitales', nuevoSignosVitales, name='signosVtalesForm'),
    path('SignosVitales/signosdetalle/<str:id>', signosDetalle, name='signosdetalle'),
    path('SignosVitales/editarSignos/<str:id>', editarSignos, name='EditarSignosVitales'),
    #Evaluacion Cuidador
    path('Evolucion/<str:rut>', login_required(evolucion), name='evolucion'),
    path('Evolucion/nuevaEvolucion/<str:rut>', nuevaEvolucion, name='evolucionForm'),
    #Reporte Excel
    path('reporte/<str:rut>', ReporteExcel.as_view(), name='reporte'),
    #Reporte PDF
    path('reportePDF/<str:rut>', ReportePDF.as_view(), name='reportePDF'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
