from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.feeding_index, name='feeding_index'),
    path('actions/', views.view_feeding_actions, name="view_feeding_actions"),
    path('actions/add/', views.add_feeding_action, name="add_feeding_action"),
    path('appointments/', views.view_feeding_appointments, name='view_feeding_appointments'),
    path('appointments/add/', views.add_feeding_appointment, name='add_feeding_appointment'),
]
