import calendar
from datetime import datetime, time, timedelta

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Exhibit, FeedingAppointment, FeedingAction

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
        actions = FeedingAction.objects.filter(exhibit=e)
        
        # is there an appointment today?
        print(datetime.now().weekday())
        appointments_today = appointments.filter(day=datetime.now().weekday())
        # if so, is there a corresponding action?
        
        grace_period = timedelta(minutes=10)
        for appointment in appointments_today:
            early_time = appointment.time - grace_period
            late_time = appointment.time + grace_period
            corresponding_action = actions.filter(date_time__time__range=(early_time, late_time))
            print(corresponding_action.count())
        
        data[e.name] = {
            'appointments': appointments,
            'actions': actions,
            'next_appointment': appointments_today,
        }

    return render(request, "zoo/feeding_appts.html", context={'data': data})