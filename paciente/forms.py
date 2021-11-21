from django import forms
from django.forms import fields
from .models import Medico, Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('n_historial','lugarAtencion','rut','Nombres','Apellidos','Direccion','nombreMedico','created_date')

class MedicoForm(forms.ModelForm):
    class Meta:
        model = Medico
        fields = ('rut', 'nombre', 'snombre', 'apellido', 'sapellido', 'direccion', 'especialidad')