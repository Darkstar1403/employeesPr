from django import forms
from .models import Paciente

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ('__all__')
        #los widget sirve para darle estilos
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder' : 'Ingrese el nombre',
                    #class etc
                }
             )
        }
    #se tiene que llamar igual que el atributo
    def clean_edad(self):
        edad = self.cleaned_data['edad']
        if(edad < 0):
            raise forms.ValidationError('Necesita tener una edad valida')
        return edad