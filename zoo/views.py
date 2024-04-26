from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Exhibit, FeedingAppointment

def index(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html')

def login_user(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return redirect('index')
    
    username = request.POST['username']
    password = request.POST['password']
    
    user = authenticate(username=username, password=password)
    if user is None:
        return redirect('index')
    
    login(request, user)
    
    return redirect('index')

def logout_user(request: HttpRequest) -> HttpResponse:
    logout(request)
    
    return redirect('index')

def animal_list(request: HttpRequest) -> HttpResponse:
    pass

def exhibit_list(request: HttpRequest) -> HttpResponse:
    pass

def exhibit_details(request: HttpRequest, id: int) -> HttpResponse:
    pass

def feeding_appointment_list(request: HttpRequest) -> HttpResponse:
    exhibits = Exhibit.objects.all()

    data = {}
    for e in exhibits:
        appointments = FeedingAppointment.objects.filter(exhibit=e)
        data[e.name] = appointments

    context = {
        'data': data
    }

    return render(request, "zoo/feeding_appts.html", context=context)