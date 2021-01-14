import re

from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
)
from .models import Empleado, Habilidades
from .forms import EmpleadoForm


# Create your views here.

class InicioView(TemplateView):
    """ Vista que carga la pagina de inicio"""
    template_name = 'inicio.html'

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 5
    ordering = "firstName"
    
    def get_queryset(self):
        palabraClave = self.request.GET.get('nombre', '')
        lista = Empleado.objects.filter(
            firstName__icontains= palabraClave
        )
        print(lista)
        return lista


class ListAllEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by = 10
    ordering = "firstName"
    context_object_name = 'empleados'
    model = Empleado


class ListByAreaEmpleado(ListView):
    template_name = 'persona/listar-por-area.html'

    def get_queryset(self):
        area = self.kwargs['shortName']
        lista = Empleado.objects.filter(
            department__shortName=area
        )
        return lista


class ListEmpleadosByKword(ListView):
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):
        palabraClave = self.request.GET.get('nombre', '')
        lista = Empleado.objects.filter(
            firstName=palabraClave
        )
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name = 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        idEmpleado = self.request.GET.get('idEmpleado')
        lista = []
        if (idEmpleado != None and re.match(r'^\d+$', idEmpleado)):
            try:
                empleado = Empleado.objects.get(id=idEmpleado)
                lista = empleado.habilidades.all()
            except ObjectDoesNotExist:
                print('Query no encontrado')
        return lista


class EmpleadoDetallesView(DetailView):
    model = Empleado
    template_name = 'persona/detalle_empleado.html'

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetallesView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = 'persona/success.html'


class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = 'persona/add.html'
    form_class = EmpleadoForm
    # ponemos la url a donde debe de ir
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # lógica del proceso
        empleado = form.save(commit=False)
        empleado.fullName = empleado.firstName + " " + empleado.lastName
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    template_name = 'persona/update.html'
    model = Empleado
    fields = ('firstName', 'lastName', 'avatar', 'job', 'department', 'habilidades', 'hoja_vida')
    success_url = reverse_lazy('persona_app:empleados_admin')

    def form_valid(self, form):
        # lógica del proceso
        print('FORM VALID')
        return super(EmpleadoUpdateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        print('POST')
        return super().post(request, *args, **kwargs)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    context_object_name = 'empleado'
    template_name = 'persona/delete.html'
    success_url = reverse_lazy('persona_app:empleados_admin')
