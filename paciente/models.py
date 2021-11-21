from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class LugarAtencion(models.Model):
    idLugarAtencion = models.AutoField(primary_key=True)
    descripcion = models.CharField('Lugar de atencion', max_length=20, null=False, blank=False)
       
    class meta:
        verbose_name = 'lugarAtencion'
        verbose_name_plural = 'LugarAtencion'
    def __str__(self):
        return self.descripcion

class Medico(models.Model):
    rut = models.CharField(primary_key=True, max_length=12)
    nombre = models.CharField('Nombres del Médico',max_length=30, null=False, blank=False)
    snombre = models.CharField('Segundo Nombre del Médico',max_length=30, null=True, blank=True)
    apellido = models.CharField('Apellido del Médico',max_length=45, null=False, blank=False)
    sapellido = models.CharField('Segundo Apellido del Médico',max_length=45, null=True, blank=True)
    direccion = models.CharField('Direccion del Médico', max_length=200)
    especialidad = models.CharField('Especialidad del Médico', max_length=200)
    created_date = models.DateTimeField('Fecha de ingreso', auto_now_add=True)
    update_date = models.DateTimeField('Fecha actualizacion', auto_now=True)
    
    class meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médico'

    def __str__(self):
        return self.nombre+' '+self.apellido


class Registro(models.Model):
    idregistro =  models.IntegerField('Numero de registro',primary_key=True)
    fecha = models.DateTimeField('Fecha de ingreso', auto_now_add=True)
    tipoAtencion = models.CharField('Tipo de Atencion', max_length=200)
    Servicio = models.CharField('Servicio', max_length=200)
    Diagnostico = models.CharField('Diagnostico', max_length=200)

    class meta:
        verbose_name = 'Registro'
        verbose_name_plural = 'Registros'

    def __str__(self):
        return self.idregistro


class Paciente(models.Model):
    lugarAtencion = models.ForeignKey(LugarAtencion, on_delete=models.CASCADE)
    rut = models.CharField(primary_key=True, max_length=12)
    Nombres = models.CharField('Nombres del paciente',max_length=30, null=False, blank=False)
    Apellidos = models.CharField('Apellidos del paciente',max_length=45, null=False, blank=False)
    Direccion = models.CharField('Direccion del paciente', max_length=200)
    nombreMedico = models.ForeignKey(Medico, on_delete=models.CASCADE,verbose_name="Nombre Médico")
    created_date = models.DateTimeField('Fecha de ingreso', default=timezone.now)
    n_historial = models.IntegerField('Numero historial')
    
    class meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.Nombres

class Historial(models.Model):
    idhistorial = models.AutoField('Id historial',primary_key=True)
    idregistro  = models.ForeignKey(Registro, on_delete=models.CASCADE)
    rut         = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'

    def __str__(self):
        return self.idhistorial