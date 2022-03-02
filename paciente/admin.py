from django import forms
from django.contrib import admin
from .models import Paciente, Medico, LugarAtencion
from django.contrib.auth.forms import ReadOnlyPasswordHashField

admin.site.register(Paciente)
admin.site.register(LugarAtencion)
admin.site.register(Medico)
