# Generated by Django 2.2.24 on 2021-11-29 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0006_auto_20211129_0035'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medico',
            name='usuario_administrador',
        ),
        migrations.AddField(
            model_name='medico',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]
