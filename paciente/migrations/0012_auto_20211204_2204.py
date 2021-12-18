# Generated by Django 2.2.24 on 2021-12-05 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paciente', '0011_auto_20211204_1527'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='Apellidos',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='Nombres',
        ),
        migrations.AddField(
            model_name='paciente',
            name='papellido',
            field=models.CharField(default='nn', max_length=45, verbose_name='Primer apellido del paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='pnombre',
            field=models.CharField(default='nn', max_length=30, verbose_name='Primer nombre del paciente'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='sapellido',
            field=models.CharField(blank=True, max_length=45, null=True, verbose_name='Segundo apellido del paciente'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='snombre',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Segundo nombre del paciente'),
        ),
    ]