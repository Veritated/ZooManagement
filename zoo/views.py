from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def user_login(request: HttpRequest) -> HttpResponse:
    pass

def user_logout(request: HttpRequest) -> HttpResponse:
    pass

def animal_list(request: HttpRequest) -> HttpResponse:
    pass

def exhibit_list(request: HttpRequest) -> HttpResponse:
    pass

def exhibit_details(request: HttpRequest, id: int) -> HttpResponse:
    pass