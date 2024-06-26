
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import permission_required

from zoo.models import HealthCondition, Diagnosis, Animal
from .forms import *

@permission_required('zoo.view_diagnosis', raise_exception=True)
def index(request: HttpRequest) -> HttpResponse:
    data = {}
    for animal in Animal.objects.all():
        untreated_diagnoses = Diagnosis.objects.filter(animal=animal, treatment_status='u')
        if untreated_diagnoses.count() < 1:
            continue
        data[animal] = untreated_diagnoses

    return render(request, 'animal_health/index.html', context={'data': data})

@permission_required('zoo.view_healthcondition', raise_exception=True)
def view_conditions(request: HttpRequest) -> HttpResponse:
    conditions = {}
    for condition in HealthCondition.objects.all():
        relevant_diagnoses = Diagnosis.objects.filter(health_condition=condition)
        # print(condition, relevant_diagnoses)
        conditions[condition] = relevant_diagnoses

    return render(request, 'animal_health/all_conditions.html', context={'conditions': conditions})

@permission_required('zoo.add_healthcondition', raise_exception=True)
def add_condition(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('index')
    
    form = AddHealthConditionForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('animal_health_index')

    return render(request, 'animal_health/add_condition.html', {'form' : form})

@permission_required('zoo.view_diagnosis', raise_exception=True)
def view_diagnoses(request: HttpRequest) -> HttpResponse:
    diagnoses = {}
    for animal in Animal.objects.all():
        relevant_diagnoses = Diagnosis.objects.filter(animal=animal)
        if relevant_diagnoses.count() < 1:
            continue
        # print(condition, relevant_diagnoses)
        diagnoses[animal] = relevant_diagnoses

    return render(request, 'animal_health/all_diagnoses.html', context={'diagnoses': diagnoses})

@permission_required('zoo.add_diagnosis', raise_exception=True)
def add_diagnoses(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('index')
    
    form = AddDiagnosisForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('animal_health_index')

    return render(request, 'animal_health/add_diagnosis.html', {'form' : form})

class UpdateDiagnosisForm(PermissionRequiredMixin, UpdateView):
    model = Diagnosis
    fields = '__all__'
    permission_required = 'zoo.change_diagnosis'