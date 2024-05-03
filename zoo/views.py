
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from .models import Animal
from .models import Exhibit
from .models import Diagnosis
from .models import FeedingAppointment
from django.contrib.auth import authenticate, login, logout

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
    animals = Animal.objects.all()
    return render(request, 'zoo/AnimalCatalog.html',{'animals': animals})

def exhibit_list(request: HttpRequest) -> HttpResponse:
    exhibits = Exhibit.objects.all()
    return render(request, 'zoo/ExhibitCatalog.html',{'exhibits' : exhibits})

def exhibit_details(request: HttpRequest, name: str) -> HttpResponse:
    exhibit = None
    for e in Exhibit.objects.all():
        if e.name == name:
            exhibit = e

    animals = []
    for a in Animal.objects.all():
        if a.exhibit == exhibit:
            animals.append(a)

    return render(request, 'zoo/SpecificExhibit.html',{'exhibit':exhibit,'animals':animals})

def animal_details(request: HttpRequest, name: str) -> HttpResponse:
     animal = Animal
     for a in Animal.objects.all():
         if a.name == name:
             animal = a

     diagnosis = []
     for d in Diagnosis.objects.all():
         if d.animal.name == animal.name:
             diagnosis.append(d)


     return render(request, 'zoo/SpecificAnimalConditions.html', {'animal':animal,'diagnosis':diagnosis})
