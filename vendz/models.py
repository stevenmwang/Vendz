from __future__ import unicode_literals

from django.db import models

"""
Vendor model that holds data fields, specifying its name and number of events
it's occured in. An arbitrary id value is specified for each vendor to allow for easy
lookup
"""
class Vendor(models.Model):
	name = models.CharField(max_length = 100)
	def __str__(self):
		return self.name
	
"""
Event model that holds data fields, specifying the details of each event.
"""
class Event(models.Model):
	name = models.CharField(max_length = 100)
	start_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	end_time = models.DateTimeField(auto_now=False, auto_now_add=False)
	timezone = models.CharField(max_length = 30)
	eventID = models.IntegerField()
	location = models.CharField(max_length = 200)
	vendors = models.ManyToManyField(Vendor)

	def __str__(self) :
		return self.name



# Create your models here.
