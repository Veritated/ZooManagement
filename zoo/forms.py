from django import forms
from .models import FeedingAction, FeedingAppointment

class AddFeedingActionForm(forms.ModelForm):
    class Meta:
        model = FeedingAction
        fields = ['exhibit', 'staff', 'date_time']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }
        
# class AddFeedingAppointmentForm(forms.ModelForm):
#     class Meta:
#         model = FeedingAppointment