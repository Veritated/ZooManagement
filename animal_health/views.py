
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'animal_health/index.html')

def view_conditions(request: HttpRequest) -> HttpResponse:
    return render(request, 'animal_health/all_conditions.html')

def add_condition(request: HttpRequest) -> HttpResponse:
    return render(request, 'animal_health/add_condition.html')