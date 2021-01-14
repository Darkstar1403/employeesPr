from django.contrib import admin
from django.urls import path
from . import views

app_name = 'departamento_app'

urlpatterns = [
    path('agregar-departamento/', views.CreateDepartamentoView.as_view(), name='nuevo_departamento'),
    path('departamento-lista/', views.DepartamentoListView.as_view(), name='department_list'),
]
