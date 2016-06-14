from django.db import models
from django.forms import ModelForm

class PlanetForm(ModelForm):
    class Meta:
        model = Planet
        fields = ['name']
