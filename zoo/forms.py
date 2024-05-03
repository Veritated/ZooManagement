from django import forms
from .models import FeedingAction

class AddFeedingActionForm(forms.ModelForm):
    class Meta:
        model = FeedingAction
        fields = "__all__"