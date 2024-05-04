
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from zoo.models import HealthCondition, Diagnosis, Animal

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'animal_health/index.html')

def view_conditions(request: HttpRequest) -> HttpResponse:
    conditions = {}
    for condition in HealthCondition.objects.all():
        relevant_diagnoses = Diagnosis.objects.filter(health_condition=condition)
        # print(condition, relevant_diagnoses)
        conditions[condition] = relevant_diagnoses

    return render(request, 'animal_health/all_conditions.html', context={'conditions': conditions})

def add_condition(request: HttpRequest) -> HttpResponse:
    return render(request, 'animal_health/add_condition.html')

def view_diagnoses(request: HttpRequest) -> HttpResponse:
    diagnoses = {}
    for animal in Animal.objects.all():
        relevant_diagnoses = Diagnosis.objects.filter(animal=animal)
        if relevant_diagnoses.count() < 1:
            continue
        # print(condition, relevant_diagnoses)
        diagnoses[animal] = relevant_diagnoses

    return render(request, 'animal_health/all_diagnoses.html', context={'diagnoses': diagnoses})

def add_diagnoses(request: HttpRequest) -> HttpResponse:
    return render(request, 'animal_health/add_diagnosis.html')