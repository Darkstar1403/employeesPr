from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view()),
    path('lista/', views.ListaHomeView.as_view()),
    path('listaPacientes/', views.ListaPacientes.as_view()),
    path('agregar/', views.CrearPaciente.as_view(), name='prueba_add'),
    path('resume-foundation/', views.ResumeFoundationView.as_view(), name='resume_foundation'),

]
