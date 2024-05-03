from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('feeding/', views.feeding_appointment_list, name='feeding_index'),
    path('feeding/actions/add/', views.add_feeding_action, name="add_feeding_action"),
    path('feeding/appointments/add/', views.add_feeding_appointment, name='add_feeding_appointment'),
]
