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

class Paciente(models.Model):
    lugarAtencion = models.ForeignKey(LugarAtencion, on_delete=models.CASCADE)
    rut = models.CharField(primary_key=True, max_length=10)
    Nombres = models.CharField('Nombres del paciente',max_length=30, null=False, blank=False)
    Apellidos = models.CharField('Apellidos del paciente',max_length=45, null=False, blank=False)
    Direccion = models.CharField('Direccion del paciente', max_length=200)
    nombreMedico = models.CharField('Nombre del medico', max_length=200)
    created_date = models.DateTimeField('Fecha de ingreso', default=timezone.now)
    
    

    class meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'
    


    def __str__(self):
        return self.Nombres
