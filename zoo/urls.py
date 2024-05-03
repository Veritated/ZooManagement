from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('animalcatalog/',views.animal_list,name='AnimalCatalog'),
    path('exhibitcatalog/',views.exhibit_list,name='ExhibitCatalog'),
    path('specificexhibit/<str:name>/',views.exhibit_details,name='SpecificExhibit'),
    path('specificanimal/<str:name>/',views.animal_details,name='SpecificAnimalConditions'),
]
