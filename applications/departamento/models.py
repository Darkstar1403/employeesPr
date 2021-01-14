from django.db import models

# Create your models here.
class Departamento(models.Model):
    name = models.CharField('Nombre', max_length=50)
    shortName = models.CharField('Nombre Corto', max_length=20)
    active = models.BooleanField('Activado', default=True)

    class Meta:
        verbose_name = 'Mi departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['name']
        #Evita los registros que tengan los mismos valores en ambos campos
        #como una llave primaria compuesta
        unique_together = ('name', 'shortName')

    def __str__(self):
        return self.name