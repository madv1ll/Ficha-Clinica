from django.shortcuts import render
from .models import Paciente

# Create your views here.
def pacienteinicio(request):
    pacientes = Paciente.objects.all()  #select * from paciente
    traspaso = {
        'pacientes':pacientes
    }
    return render(request, 'index.html', traspaso)

def historial(request, rut):
    pacientes = Paciente.objects.filter(rut = rut)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'historial.html',datos)


