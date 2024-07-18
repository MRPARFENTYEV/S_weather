from .models import User, UserQuery
from django import forms

class InputCityForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Введите название города'}
        )
    )