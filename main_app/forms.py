from django import forms
from .models import GameSession, Location

class GameSessionForm(forms.ModelForm):
    class Meta:
        model = GameSession
        fields = ['date', 'power_up']
        widgets = {
            'date': forms.DateInput(
                format=('%Y-%m-%d'),
                attrs={
                    'placeholder': 'Select a Date',
                    'type': 'date'
                }
            ),
        }
