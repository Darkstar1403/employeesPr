from django.contrib import admin
from .models import Empleado, Habilidades

# Register your models here.


admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'firstName',
        'lastName',
        'department',
        'job',
        'full_name',
    )
    def full_name(self,obj):
        nombreCompleto = obj.firstName + ' ' + obj.lastName
        return nombreCompleto
    search_fields = ('firstName',)
    list_filter = ('department' ,'job', 'habilidades')
    #este filter solo sirve para campos relacionados
    filter_horizontal = ('habilidades',)

admin.site.register(Empleado, EmpleadoAdmin)