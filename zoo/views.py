from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.contrib.auth import authenticate, login, logout

from zoo.forms import *

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

def new_animal(request: HttpRequest) -> HttpRequest:
    if not request.user.is_authenticated:
        return redirect('index')
    
    form = AddNewAnimalForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('index')

    return render(request, 'zoo/newanimal.html', {'form' : form})