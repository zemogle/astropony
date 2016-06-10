from django.db import models


class Mission(models.Model):
    name = models.CharField(max_length=200)
    start_date = models.DateTimeField('date discovered')

    def __unicode__(self):
    	return self.name

class Planet(models.Model):
    name = models.CharField(max_length=200)
    discovery_date = models.DateTimeField('date discovered')
    mass = models.FloatField()
    radius = models.FloatField()
    misson = models.ForeignKey(Mission)

    def __unicode__(self):
    	return self.name

