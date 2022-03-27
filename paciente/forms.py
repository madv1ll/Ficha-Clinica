from django import forms
from .models import Evaluacion, Historial, Medico, Paciente, SignosVitales

class PacienteForm(forms.ModelForm):
    cuidadores = Medico.objects.all()
    class Meta:
        model = Paciente
        fields = ['lugarAtencion','rut','pnombre','snombre','papellido','sapellido','Direccion','fecha_nacimiento','nombreMedico']

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
        fields = ('temperatura','respiracion','presion_arterial','evaluacion','miccion','vomito','flatos','dolor','estrennimiento','frecuencia_cardiaca','saturacion',
                'suenno',
                'presion_arterial_media',
                'peso',
                'talla',
                'alimentacion',
                'higiene',
                'observaciones')

class HistorialForm(forms.ModelForm):
    class Meta:
        model = Historial
        fields = ('tipo_atencion',
                  'servicio',
                  'diagnostico',
                  'motivo_ingreso',
                  'enfermedad_actual',
                  'diagnostico_admision',
                  'diagnostico_clinico_final', 
                  'fecha_alta_medica', 
                  'fecha_alta_clinica')

class EvolucionForm(forms.ModelForm):
    class Meta:
        model = Evaluacion
        fields = ('cuidador','descripcion')

