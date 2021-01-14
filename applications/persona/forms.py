from django import forms

from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    """Form definition for Empleado."""

    class Meta:
        """Meta definition for Empleadoform."""

        model = Empleado
        fields = (
            'firstName',
            'lastName',
            'job',
            'department',
            'avatar',
            'habilidades',
            'hoja_vida',
        )
        widgets = {
            'habilidades' : forms.CheckboxSelectMultiple()
        }
