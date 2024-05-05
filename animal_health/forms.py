from django import forms
from django.views.generic.edit import UpdateView

from zoo.models import HealthCondition, Diagnosis

class AddHealthConditionForm(forms.ModelForm):
    class Meta:
        model = HealthCondition
        fields = '__all__'
        
class AddDiagnosisForm(forms.ModelForm):
    class Meta:
        model = Diagnosis
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'})
        }
