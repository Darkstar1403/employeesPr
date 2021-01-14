from django.db import models

from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.

class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    def __str__(self):
        return self.habilidad

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades de empleado'

class Empleado(models.Model):
    trabajos = [
        ['0','Contador'],['1','Administrador'],
        ['2', 'Economista'], ['3', 'Otro']
    ]
    firstName = models.CharField('Nombres', max_length=60)
    lastName = models.CharField('Apellidos', max_length=60)
    fullName = models.CharField('Nombre completo', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=trabajos)
    department = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', null=True, blank=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    class Meta:
        verbose_name = 'El empleado'
        verbose_name_plural = 'Los empleados'
        ordering = ['job']
        unique_together = ('firstName', 'lastName', 'department')

    def __str__(self):
        return str(self.id) + ' ' + self.firstName + ' ' + self.lastName
