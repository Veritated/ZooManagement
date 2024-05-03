from django import forms
from .models import Animal, FeedingAction, FeedingAppointment

class AddFeedingActionForm(forms.ModelForm):
    class Meta:
        model = FeedingAction
        fields = ['exhibit', 'staff', 'date_time']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}),   
        }
        labels = {
            'date_time': 'Date & Time'
        }
        
class AddFeedingAppointmentForm(forms.ModelForm):
    class Meta:
        model = FeedingAppointment
        fields = ['exhibit', 'day', 'time']
        widgets = {
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

class AddNewAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'birth_date', 'death_date', 'description', 'species', 'exhibit']
        widgets = {
            'birth_date': forms.SelectDateWidget(),
            'death_date': forms.SelectDateWidget()
        }