from .models import User, UserQuery
from django import forms

class InputCityForm(forms.Form):
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Input City Title For The Weather to Know'}
        )
    )