from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Historial, LugarAtencion, Medico, Paciente, SignosVitales
from .forms import HistorialForm, MedicoForm, PacienteForm,  SignosForm
from django.shortcuts import redirect
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

def pacienteinicio(request):
    pacientes = Paciente.objects.filter(nombreMedico_id = request.user)
    page = request.GET.get('page', 1)

    paginator = Paginator(pacientes, per_page=10)
    try:
        pacientes = paginator.page(page)
    except PageNotAnInteger:
        pacientes = paginator.page(10)
    except EmptyPage:
        pacientes = paginator.page(paginator.num_pages)

    traspaso = {
        'pacientes':pacientes
    }
    return render(request, 'index.html' ,traspaso,{ 'pacientes': pacientes })

def historial(request, rut):
    pacientes = Paciente.objects.filter(rut = rut)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'historial.html',datos)

def clinica(request):
    pacientes = Paciente.objects.filter(lugarAtencion_id = 1)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'clinica.html', datos)

def domicilio(request):
    pacientes = Paciente.objects.filter(lugarAtencion_id = 2)
    datos = {
        'pacientes':pacientes
    }
    return render(request, 'domicilio.html', datos)

def nuevoPaciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.nombreMedico = request.user
            post.save()
            return redirect ('index')
    else:
        form = PacienteForm
    return render(request, 'nuevopaciente.html', {'form':form})

def editarPaciente(request, rut):
    post = get_object_or_404(Paciente, rut=rut)
    if request.method == "POST":
        form = PacienteForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PacienteForm(instance=post)
    return render(request, 'editarpaciente.html', {'form': form})

def eliminarPaciente(request, rut):
    paciente = Paciente.objects.get(rut=rut)
    paciente.delete()
    return redirect('index')

class NuevoMedico(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'nuevomedico.html'
    success_url = reverse_lazy('index')


class SignosVitalesView(CreateView):
    model = SignosVitales
    form_class = SignosForm
    template_name = 'signosVitales.html'
    success_url = reverse_lazy('index')

class NuevoSignosVitales(CreateView):
    model = SignosVitales
    form_class = SignosForm
    template_name = 'signosVitalesForm.html'
    success_url = reverse_lazy('index')

class SignosViews(ListView):
    model = SignosVitales
    template_name = 'signosVitales.html'
    


 

class NuevoHistorial(CreateView):
    model = Historial
    form_class = HistorialForm
    template_name = 'HistorialForm.html'
    success_url = reverse_lazy('historial')




