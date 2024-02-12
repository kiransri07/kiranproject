from django.forms import ModelForm,TextInput
from .models import city

class CityForm(ModelForm):
    class Meta:
        model=city
        fielde=["name"]
        widgets={'name':TextInput(attrs={'class':'form-contol','placeholder': 'city Name'})}