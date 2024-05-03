import calendar
from datetime import datetime, time, timedelta

from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout

from .models import Exhibit, FeedingAppointment, FeedingAction
from .forms import AddFeedingActionForm

APPOINTMENT_GRACE_PERIOD = timedelta(minutes=10)

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
    if not request.user.is_authenticated:
        return redirect('index')
    
    data = {}
    for exhibit in Exhibit.objects.all():
        appointments_today = FeedingAppointment.objects.filter(exhibit=exhibit).filter(day=datetime.now().weekday())
        appointments_today = appointments_today.order_by('time')
        actions_today = FeedingAction.objects.filter(exhibit=exhibit).filter(date_time__date=datetime.today())
        
        # have any appointments already been taken care of?
        unfulfilled_appointments = {}
        for appointment in appointments_today:
            appointment_date_time = datetime.combine(datetime.today(), appointment.time)
            late_time = appointment_date_time + APPOINTMENT_GRACE_PERIOD
            early_time = appointment_date_time - APPOINTMENT_GRACE_PERIOD
            corresponding_actions = actions_today.filter(date_time__time__range=(early_time, late_time))
            
            # print(corresponding_actions.count(), appointment.formatted_time)
            if corresponding_actions.count() > 1:
                print('possible overfeeding')
            elif corresponding_actions.count() > 0:
                continue
            
            is_late = datetime.now() > appointment_date_time
            unfulfilled_appointments[appointment] = is_late
        
        data[exhibit.name] = {
            'appointments': appointments_today,
            'actions': actions_today,
            'unfulfilled_appts': unfulfilled_appointments,
        }

    return render(request, "zoo/feeding_appts.html", context={'data': data})

def add_feeding_action(request: HttpRequest) -> HttpResponse:
    if not request.user.is_authenticated:
        return redirect('index')
    
    form = AddFeedingActionForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('feeding_index')

    return render(request, 'zoo/add_feeding_action.html', {'form' : form})