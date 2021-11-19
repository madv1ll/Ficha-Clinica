from django.shortcuts import render
from .models import Paciente
from django.http import HttpResponse



# Create your views here.
def pacienteinicio(request):
    pacientes = Paciente.objects.all()  #select * from paciente
    traspaso = {
        'pacientes':pacientes
    }
    return render(request, 'index.html', traspaso)

def historial(request, rut):
    pacientes = rut
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'historial.html',datos)


