from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import  AbstractUser, UserManager

class LugarAtencion(models.Model):
    idLugarAtencion = models.AutoField(primary_key=True)
    descripcion     = models.CharField('Lugar de atencion', max_length=20, null=False, blank=False)
       
    class meta:
        verbose_name = 'lugarAtencion'
        verbose_name_plural = 'LugarAtencion'
    def __str__(self):
        return self.descripcion


class MedicoManager(UserManager):
    def create_user(self,rut,nombre,snombre,apellido, sapellido, direccion, especialidad,username,password = None):
        usuario = self.model(
            username     = username,
            rut          = rut,
            nombre       = nombre,
            snombre      = snombre,
            apellido     = apellido,
            sapellido    = sapellido,
            direccion    = direccion,
            especialidad = especialidad
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,rut,nombre,snombre,apellido, sapellido, direccion, especialidad,username,password):
        usuario = self.create_user(
            username     = username,
            rut          = rut,
            nombre       = nombre,
            snombre      = snombre,
            apellido     = apellido,
            sapellido    = sapellido,
            direccion    = direccion,
            especialidad = especialidad
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario


class Medico(AbstractUser):
    rut          = models.CharField(primary_key=True, max_length=12)
    nombre       = models.CharField('Nombres del Cuidador',max_length=30, null=False, blank=False)
    snombre      = models.CharField('Segundo Nombre del Cuidador',max_length=30, null=True, blank=True)
    apellido     = models.CharField('Apellido del Cuidador',max_length=45, null=False, blank=False)
    sapellido    = models.CharField('Segundo Apellido del Cuidador',max_length=45, null=True, blank=True)
    direccion    = models.CharField('Direccion del Cuidador', max_length=200)
    especialidad = models.CharField('Especialidad del Cuidador', max_length=200)
    created_date = models.DateTimeField('Fecha de ingreso', auto_now_add=True)
    update_date  = models.DateTimeField('Fecha actualizacion', auto_now=True)
    username     = models.CharField('Nombre de Usuario', unique=True, max_length=50) 
    
    USERNAME_FIELD = 'username'

    class meta:
        verbose_name = 'Médico'
        verbose_name_plural = 'Médico'

    def __str__(self):
        return self.nombre+' '+self.apellido
    
    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self, app_label):
        return True
class Paciente(models.Model):
    lugarAtencion     = models.ForeignKey(LugarAtencion, on_delete=models.CASCADE)
    rut               = models.CharField(primary_key=True, max_length=12)
    pnombre           = models.CharField('Primer nombre del paciente',max_length=30, null=False, blank=False)
    snombre           = models.CharField('Segundo nombre del paciente',max_length=30, null=True, blank=True)
    papellido         = models.CharField('Primer apellido del paciente',max_length=45, null=False, blank=False)
    sapellido         = models.CharField('Segundo apellido del paciente',max_length=45, null=True, blank=True)
    Direccion         = models.CharField('Direccion del paciente', max_length=200)
    fecha_nacimiento  = models.DateTimeField('Fecha de Nacimiento', null=False)
    nombreMedicoAdmin = models.CharField('Nombre Medico', null=False, default='cuidador',max_length=45)
    nombreMedico      = models.CharField('Nombre Medico', null=False,  default='cuidador',max_length=45)
    created_date      = models.DateTimeField('Fecha de ingreso', default=timezone.now)
    
    class meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.rut


class Historial(models.Model):
    idhistorial               = models.AutoField('Id historial',primary_key=True)
    fecha                     = models.DateTimeField('Fecha de registro', auto_now=True)
    tipo_atencion             = models.ForeignKey(LugarAtencion, on_delete=models.CASCADE)
    servicio                  = models.CharField('Servicio', max_length=30, null=True, blank=True)
    diagnostico               = models.CharField('Diagnostico', max_length=150, null=True, blank=True)
    motivo_ingreso            = models.CharField('Motivo de ingreso', max_length=150, null=True, blank=True) 
    enfermedad_actual         = models.CharField('Enfermedad actual', max_length=150, null=True, blank=True) 
    diagnostico_admision      = models.CharField('Diagnostico de admision', max_length=150, null=True, blank=True)
    diagnostico_clinico_final = models.CharField('Diagnostico clinico final', max_length=200, null=True, blank=True)
    fecha_alta_medica         = models.DateTimeField('Fecha alta Medica',  null=True, blank=True)
    fecha_alta_clinica        = models.DateTimeField('Fecha alta clinica',  null=True, blank=True)
    rut                       = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'

    def __str__(self):
        return self.idhistorial



class SignosVitales(models.Model):
    id_signosvitales          = models.AutoField('id signos vitales', primary_key=True)
    fecha_creacion            = models.DateTimeField('Fecha registro', auto_now=True)
    presion_arterial          = models.CharField('Tension', null=True, max_length=50, blank=True)
    presion_arterial_media    = models.CharField('Presión Arterial Media', null=True, max_length=50, blank=True)
    respiracion               = models.CharField('Respiracion', null=True, max_length=50, blank=True)
    frecuencia_cardiaca       = models.CharField('Frecuencia Cardiaca', null=True, max_length=50, blank=True)
    temperatura               = models.CharField('Temperatura', null=True, max_length=50, blank=True)
    saturacion                = models.CharField('Saturacion', null=True, max_length=50, blank=True)
    peso                      = models.CharField('Peso', null=True, max_length=50, blank=True)
    talla                     = models.CharField('Talla', null=True, max_length=50, blank=True)
    evaluacion                = models.CharField('Evaluacion', null=True, max_length=150, blank=True)
    miccion                   = models.CharField('Miccion', null=True, max_length=150, blank=True)
    vomito                    = models.CharField('Vomito', null=True, max_length=150, blank=True)
    flatos                    = models.CharField('Flatos', null=True, max_length=50, blank=True)
    dolor                     = models.CharField('Dolor', null=True, max_length=50, blank=True)
    estrennimiento            = models.CharField('Estreñimiento', null=True, max_length=100, blank=True)
    suenno                    = models.CharField('sueño', null=True, max_length=50, blank=True)
    alimentacion              = models.CharField('Alimentacion', null=True, max_length=50, blank=True)
    higiene                   = models.CharField('Higiene', null=True, max_length=50, blank=True)
    observaciones             = models.CharField('Observaciones', null=True, max_length=50, blank=True)
    paciente_rut              = models.ForeignKey(Paciente,on_delete=models.CASCADE)
    class meta:
        verbose_name = 'Signos Vitales'
        verbose_name_plural = 'Signos Vitales'

    def __str__(self):
        return self.id_signosvitales
      
class Evaluacion(models.Model):
    idevaluacion     = models.AutoField('Id evaluacion', primary_key=True)
    fecha_evaluacion = models.DateTimeField('Fecha de evaluacion', null=False, auto_now=True)
    hora             = models.DateTimeField('Hora evolucion', null=False, auto_now=True)
    cuidador         = models.CharField('Cuidador', max_length=30)
    descripcion      = models.TextField('Descripcion', max_length=2000)
    rut              = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'

    def __str__(self):
        return self.idevaluacion

