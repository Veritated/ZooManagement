
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='animal_health_index'),
    path('conditions/', views.view_conditions, name='view_conditions'),
    path('conditions/add/', views.add_condition, name='add_condition'),
    path('diagnoses/', views.view_diagnoses, name='view_diagnoses'),
    path('diagnoses/add/', views.add_diagnoses, name='add_diagnosis'),
    path('diagnoses/<int:pk>/update/', views.UpdateDiagnosisForm.as_view(), name='update_diagnosis')
]
