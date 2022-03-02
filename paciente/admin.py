from django import forms
from django.contrib import admin
from .models import Paciente, Medico, LugarAtencion
from django.contrib.auth.forms import ReadOnlyPasswordHashField

admin.site.register(Paciente)
admin.site.register(LugarAtencion)
admin.site.register(Medico)

class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ''

    class Meta:
        model = Medico
        fields = ('__all__')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]
