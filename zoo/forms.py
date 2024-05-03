from django import forms
from .models import Animal

class AddNewAnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'birth_date', 'death_date', 'description', 'species', 'exhibit']
        widgets = {
            'birth_date': forms.SelectDateWidget(),
            'death_date': forms.SelectDateWidget()
        }