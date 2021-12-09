from django.forms.models import model_to_dict
from django.http import  JsonResponse
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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils import timezone

def historial(request, rut):
    pacientes = Paciente.objects.filter(rut = rut)
    historial = Historial.objects.filter(rut = rut)
    datos = {
        'pacientes':pacientes,
        'historial':historial
    }
    return render(request, 'historial.html',datos)

def historialDetalle(request, id):
    historialobj = Historial.objects.filter(idhistorial = id)
    datos = {
        'historial': historialobj
    }
    return render(request, 'historialdetalle.html',datos)


def nuevoPaciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.nombreMedico = request.user.username
            post.nombreMedicoAdmin = 'cuidador'
            post.save()
            return redirect ('index')
    else:
        form = PacienteForm
    return render(request, 'nuevopaciente.html', {'form':form})

    #Nuevo Historial VBF
def nuevoHistorialf(request, rut):
    obj = get_object_or_404(Paciente, rut=rut)
    form = HistorialForm(request.POST, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit = False)
            post.rut = obj.rut
            post.save()
            return redirect ('historial_clinico',rut)
    else:
        form = HistorialForm
    return render(request, 'HistorialForm.html', {'form':form})

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

def eliminarPaciente(request,rut):
    paciente = Paciente.objects.filter(rut=rut)
    paciente.delete()
    messages.success(request, 'Paciente elminado con éxito')

    return redirect('index')

def pacienteinicio(request):
    pacientes = Paciente.objects.filter(nombreMedico_id = request.user)
    traspaso = {
        'pacientes':pacientes
    }
    # if request.method == "POST":
    #     return HttpResponse(Paciente.objects.filter(nombreMedico_id = 1))
    return render(request, 'index.html' ,traspaso)

def signosVitales(request, rut):
    pacientes = Paciente.objects.filter(rut = rut)
    signos = SignosVitales.objects.filter(paciente_rut = rut)
    datos = {
        'pacientes':pacientes,
        'signosVitales': signos
    }
    return render(request, 'signosVitales.html',datos)

def nuevoSignosVitales(request, rut):
    obj = get_object_or_404(Paciente, rut=rut)
    form = SignosForm(request.POST, instance=obj)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit = False)
            post.paciente_rut = obj.rut
            post.save()
            return redirect ('signosVitales.html',rut)
    else:
        form = SignosForm
    return render(request, 'signosVitales.html', {'form':form})


class NuevoMedico(CreateView):
    model = Medico
    form_class = MedicoForm
    template_name = 'nuevomedico.html'
    success_url = reverse_lazy('index')


class NuevoSignosVitales(CreateView):
    model = SignosVitales
    form_class = SignosForm
    template_name = 'signosVitalesForm.html'
    success_url = reverse_lazy('index')

class SignosViews(ListView):
    model = SignosVitales
    template_name = 'signosVitales.html'

# class NuevoHistorial(CreateView):
#     model = Historial
#     form_class = HistorialForm
#     template_name = 'HistorialForm.html'
#     success_url = reverse_lazy('historial')

class Index(CreateView):
    model = Paciente
    fields = ('__all__')
    template_name = 'index.html'
    success_url = '.'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        user = request.user.username
        print('usuario: ',user)
        data = list(Paciente.objects.filter(lugarAtencion=request.POST['id']).filter(nombreMedico=user).values())
        return JsonResponse({'lugaratencion':data})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lugarSeleccion"] = Paciente.objects.filter(lugarAtencion=1)
        return context