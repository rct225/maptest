from django.db import models

# Create your models here.
class Locations(models.Model):
    locationName = models.CharField(max_length=200, blank=True)
    latitude = models.CharField(max_length=25, blank=True)
    longitute = models.CharField(max_length=25, blank=True)
    locationAddress = models.CharField(max_length=55, blank=True)
    
    def __unicode__(self):
        return self.locationName

