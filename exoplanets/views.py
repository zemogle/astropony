from django.shortcuts import render
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from exoplanets.models import Planet
from .models import *

def home(request):
	no_exoplanets = Planet.objects.all().count()
	return render(request,'exoplanets/index.html',{'no_exoplanets': no_exoplanets})

def planets(request):
	planets = Planet.objects.all()
	return render(request,'exoplanets/planets.html',{'planets':planets})

class PlanetUpdate(UpdateView):
    model = Planet
    fields = ['name']
    template_name = 'exoplanets/planet_update.html'

class PlanetDetails(DetailView):
    model = Planet
    template_name = 'exoplanets/planet.html'
