from django import forms
from django.forms import fields
from .models import Historial, Medico, Paciente, SignosVitales
from django.contrib.auth.forms import AuthenticationForm

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('n_historial','lugarAtencion','rut','Nombres','Apellidos','Direccion','fecha_nacimiento')


class MedicoForm(forms.ModelForm):
    password = forms.CharField(label= 'Contraseña', widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder':'Ingrese Contraseña',
            'id': 'password'
        }
    ))
    class Meta:
        model = Medico
        fields = ('rut', 'nombre', 'snombre', 'apellido', 'sapellido', 'direccion', 'especialidad','username',)



    def clean_password2(self):
        password = self.cleaned_data.get('password')
        return password
 
    def save(self,commit = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            return user


class SignosForm(forms.ModelForm):
    class Meta:
        model = SignosVitales
        fields = ('__all__')

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ('fecha','tipo_atencion','servicio','diagnostico','motivo_ingreso','enfermedad_actual','diagnostico_admision','diagnostico_clinico_final', 'fecha_alta_medica', 'fecha_alta_clinica')

