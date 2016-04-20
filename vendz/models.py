from __future__ import unicode_literals

from django.db import models

class Vendor(models.Model):
	name = models.CharField(max_length = 100)
	occurances = models.IntegerField(default = 0)
	vendor_id = models.IntegerField(default = 0, primary_key = True)
	def __str__(self) :
		return self.name
	

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
