from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, BaseUserManager, User, UserManager

class LugarAtencion(models.Model):
    idLugarAtencion = models.AutoField(primary_key=True)
    descripcion = models.CharField('Lugar de atencion', max_length=20, null=False, blank=False)
       
    class meta:
        verbose_name = 'lugarAtencion'
        verbose_name_plural = 'LugarAtencion'
    def __str__(self):
        return self.descripcion

class MedicoManager(UserManager):
    def create_user(self,rut,nombre,snombre,apellido, sapellido, direccion, especialidad,username,password = None):
        usuario = self.model(
            username = username,
            rut=rut,
            nombre = nombre,
            snombre = snombre,
            apellido = apellido,
            sapellido = sapellido,
            direccion = direccion,
            especialidad = especialidad
        )
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self,rut,nombre,snombre,apellido, sapellido, direccion, especialidad,username,password):
        usuario = self.create_user(
            username = username,
            rut=rut,
            nombre = nombre,
            snombre = snombre,
            apellido = apellido,
            sapellido = sapellido,
            direccion = direccion,
            especialidad = especialidad
        )
        usuario.usuario_administrador = True
        usuario.save()
        return usuario

class Medico(AbstractUser):
    rut          = models.CharField(primary_key=True, max_length=12)
    nombre       = models.CharField('Nombres del Médico',max_length=30, null=False, blank=False)
    snombre      = models.CharField('Segundo Nombre del Médico',max_length=30, null=True, blank=True)
    apellido     = models.CharField('Apellido del Médico',max_length=45, null=False, blank=False)
    sapellido    = models.CharField('Segundo Apellido del Médico',max_length=45, null=True, blank=True)
    direccion    = models.CharField('Direccion del Médico', max_length=200)
    especialidad = models.CharField('Especialidad del Médico', max_length=200)
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
    fecha_nacimiento = models.DateTimeField('Fecha de Nacimiento', null=False)
    nombreMedico = models.ForeignKey(Medico, on_delete=models.CASCADE,verbose_name="Nombre Médico" )
    created_date = models.DateTimeField('Fecha de ingreso', default=timezone.now)
    n_historial = models.IntegerField('Numero historial')
    
    class meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return self.Nombres

class Historial(models.Model):
    idhistorial = models.AutoField('Id historial',primary_key=True)
    fecha = models.DateTimeField('Fecha de registro', default=timezone.now)
    tipo_atencion = models.CharField('Tipo de atencion', max_length=50)
    servicio = models.CharField('Servicio', max_length=30)
    diagnostico = models.CharField('Diagnostico', max_length=150)
    motivo_ingreso = models.CharField('Motivo de ingreso', max_length=150) 
    enfermedad_actual = models.CharField('Enfermedad actual', max_length=150) 
    diagnostico_admision = models.CharField('Diagnostico de admision', max_length=150)
    diagnostico_clinico_final = models.CharField('Diagnostico clinico final', max_length=200)
    fecha_alta_medica = models.DateTimeField('Fecha alta Medica', null=False)
    fecha_alta_clinica = models.DateTimeField('Fecha alta clinica', null=False)
    rut         = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    class meta:
        verbose_name = 'Historial'
        verbose_name_plural = 'Historial'

    def __str__(self):
        return self.idhistorial

class evaluacion(models.Model):
    idevaluacion = models.AutoField('Id evaluacion', primary_key=True)
    fecha_evaluacion = models.DateTimeField('Fecha de evaluacion', null=False)
    descripcion = models.CharField('Descripcion', max_length=200)
    rut = models.ForeignKey(Paciente, on_delete=models.CASCADE)


    class meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'

    def __str__(self):
        return self.idevaluacion