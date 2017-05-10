from django.shortcuts import render
from .models import *

def home(request):
    return render(request,'exoplanets/index.html',{})

def planets(request):
    planets = Planet.objects.all()
    return render(request,'exoplanets/planets.html',{'planets':planets})
