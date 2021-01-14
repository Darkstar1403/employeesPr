from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
# Create your views here.
from .forms import NewDepartamentoForm
from applications.persona.models import Empleado
from .models import Departamento


class CreateDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = reverse_lazy('departamento_app:department_list')

    def form_valid(self, form):
        dep = Departamento(
            name= form.cleaned_data['departamento'],
            shortName = form.cleaned_data['shortName']
        )
        dep.save()
        nombre = form.cleaned_data['nombre']
        apellidos = form.cleaned_data['apellidos']
        Empleado.objects.create(
            firstName = nombre,
            lastName = apellidos,
            fullName= nombre + " " + apellidos,
            job='1',
            department =dep
        )
        return super(CreateDepartamentoView,self).form_valid(form)


class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/lista.html"
