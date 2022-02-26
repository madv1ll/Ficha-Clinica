from urllib import response
from django.forms.models import model_to_dict
from django.http import  JsonResponse
from django.db.models import query
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Evaluacion, Historial, LugarAtencion, Medico, Paciente, SignosVitales
from .forms import EvolucionForm, HistorialForm, MedicoForm, PacienteForm,  SignosForm
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from django.views.generic.base import TemplateView
from openpyxl import Workbook
from openpyxl.styles import Alignment,Border,Font,PatternFill,Side

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

def nuevoHistorialf(request, rut):
    form = HistorialForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit = False)
            post.rut_id = rut
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
    form = SignosForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit = False)
            post.paciente_rut_id = rut
            post.save()
            return redirect ('signosVitales',rut)
    else:
        form = SignosForm
    return render(request, 'signosVitalesForm.html', {'form':form})

def signosDetalle(request, id):
    signos = SignosVitales.objects.filter(id_signosvitales = id)
    datos = {
        'signos': signos
    }
    return render(request, 'signosdetalle.html',datos)

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

def editarHistorial(request, id):
    post = get_object_or_404(Historial, idhistorial=id)
    if request.method == "POST":
        form = HistorialForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = HistorialForm(instance=post)
    return render(request, 'editarHistorial.html', {'form': form})

def editarSignos(request, id):
    post = get_object_or_404(SignosVitales, id_signosvitales=id)
    if request.method == "POST":
        form = SignosForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignosForm(instance=post)
    return render(request, 'editarSignos.html', {'form': form})

class Index(CreateView):
    model = Paciente
    fields = ('__all__')
    template_name = 'index.html'
    success_url = '.'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        queryset = request.POST["buscar"]
        if queryset:
            data = list(Paciente.objects.filter(Q(rut__icontains=queryset) | Q(pnombre__icontains=queryset) | Q(papellido__icontains=queryset) ).distinct().values())
        else:
            data = list(Paciente.objects.filter(lugarAtencion=request.POST['id']).values())
        return JsonResponse({'lugaratencion':data})
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["lugarSeleccion"] = Paciente.objects.filter(lugarAtencion=1)
        return context

def evolucion(request, rut):
    pacientes = Paciente.objects.filter(rut = rut)
    evaluacion = Evaluacion.objects.filter(rut = rut)
    datos = {
        'pacientes':pacientes,
        'evolucion':evaluacion
    }
    return render(request, 'evolucion.html',datos)

def nuevaEvolucion(request, rut):
    form = EvolucionForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            post = form.save(commit = False)
            post.rut_id = rut
            fecha = timezone.now()
            convertida = fecha.strftime("%d-%m-%Y")
            post.fecha_evaluacion = convertida
            post.hora = fecha.strftime('%H:%M')
            post.save()
            return redirect ('evolucion', rut)
    else:
        form = EvolucionForm
    return render(request, 'evolucionForm.html', {'form':form})

class ReporteExcel(TemplateView):
    def get(self, request, *args, **kwargs):
        query = Paciente.objects.all()
        wb = Workbook()
        bandera = True
        cont = 1
        controlador = 4
        for q in query:
            if bandera:
                ws = wb.active
                ws.title = 'Hoja'+str(cont)
                bandera = False
            else:
                ws = wb.create_sheet('Hoja'+str(cont))
            ws['B1'].alignment = Alignment(horizontal= "center", vertical= "center")
            ws['B1'].border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                     top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws['B1'].fill = PatternFill(start_color= '66FFCC', end_color= '66FFCC', fill_type= "solid")
            ws['B1'].font = Font(name = 'Calibri', size = 12, bold= True)
            ws['B1'] = 'Reporte Excel'

            #dimesiones de la tabla 
            ws.merge_cells('B1:D1')
            ws.row_dimensions[1].height = 25
            ws.column_dimensions['B'].width = 20
            ws.column_dimensions['C'].width = 20
            ws.column_dimensions['D'].width = 20

            ws['B3'].alignment = Alignment(horizontal= "center", vertical= "center")
            ws['B3'].border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                     top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws['B3'].fill = PatternFill(start_color= '66FFCC', end_color= '66FFCC', fill_type= "solid")
            ws['B3'].font = Font(name = 'Calibri', size = 10, bold= True)
            ws['B3'] = 'Rut'

            ws['C3'].alignment = Alignment(horizontal= "center", vertical= "center")
            ws['C3'].border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                     top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws['C3'].fill = PatternFill(start_color= '66FFCC', end_color= '66FFCC', fill_type= "solid")
            ws['C3'].font = Font(name = 'Calibri', size = 10, bold= True)
            ws['C3'] = 'Nombres'

            ws['D3'].alignment = Alignment(horizontal= "center", vertical= "center")
            ws['D3'].border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                     top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws['D3'].fill = PatternFill(start_color= '66FFCC', end_color= '66FFCC', fill_type= "solid")
            ws['D3'].font = Font(name = 'Calibri', size = 10, bold= True)
            ws['D3'] = 'Apellidos'


            #tabla dinamica con los datos
            ws.cell(row = controlador, column= 2).alignment = Alignment(horizontal = "center")
            ws.cell(row = controlador, column= 2).border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                                                  top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws.cell(row = controlador, column= 2).font = Font(name = 'Calibri', size = 10)
            ws.cell(row = controlador, column= 2).value = q.rut

            ws.cell(row = controlador, column= 3).alignment = Alignment(horizontal = "center")
            ws.cell(row = controlador, column= 3).border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                                                  top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws.cell(row = controlador, column= 3).font = Font(name = 'Calibri', size = 10)
            ws.cell(row = controlador, column= 3).value = q.pnombre +' '+ q.snombre

            ws.cell(row = controlador, column= 4).alignment = Alignment(horizontal = "center")
            ws.cell(row = controlador, column= 4).border = Border(left = Side(border_style= "thin"), right = Side(border_style= "thin"),
                                                                  top  = Side(border_style= "thin"), bottom = Side(border_style= "thin"))
            ws.cell(row = controlador, column= 4).font = Font(name = 'Calibri', size = 10)
            ws.cell(row = controlador, column= 4).value = q.papellido +' '+ q.sapellido
            cont += 1
        nombre_archivo = "ReporteExcel.xlsx"
        response = HttpResponse(content_type = "application/ms-excel")
        contenido = "attachment; filename = {0}".format(nombre_archivo)
        response["Content-Disposition"] = contenido
        wb.save(response)
        return response
