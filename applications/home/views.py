from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
)
from .forms import PacienteForm


# Create your views here.
from .models import Paciente


class HomeView(TemplateView):
    template_name = 'home/home.html'

class ResumeFoundationView(TemplateView):
    template_name = 'home/resume_foundation.html'

class ListaHomeView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'nombres'
    queryset = ['Pedro', 'Juan', 'Alberto', 'Sech']

class ListaPacientes(ListView):
    template_name = 'home/listaPacientes.html'
    model = Paciente
    context_object_name = 'nombresPacientes'

class CrearPaciente(CreateView):
    template_name = 'home/add.html'
    model = Paciente
    form_class = PacienteForm
    success_url = '/'

