from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Event, Vendor
from django.core.urlresolvers import reverse
from django.views import generic
from datetime import datetime
from django.utils import timezone
import json
import urllib2
from collections import defaultdict
import operator


def index(request):
	populateDatabase()
	return render(request, 'vendz/index.html')

def events(request):
	upcomingEvents = Event.objects.filter(end_time__gt=datetime.now()) 
	pastEvents = Event.objects.filter(end_time__lt=datetime.now()) 
	context = {'upcomingEvents' : upcomingEvents, 
				'pastEvents' : pastEvents}
	return render(request, 'vendz/events.html', context)

def vendors(request):
	vendor_dict = {}
	vendor_list = Vendor.objects.all()
	for vendor in vendor_list:
		vendor_dict[vendor.name] = [vendor.id, 0]
	pastEvents = Event.objects.filter(end_time__lt=datetime.now()) 
	for event in pastEvents:
		vendors = event.vendors.all()
		for vendor in vendors:
			vendor_dict[vendor.name][1] += 1 
	
	vendor_dict = reversed(sorted(vendor_dict.items(), key=lambda(k,v): operator.itemgetter(1)(v)))
	context = {'vendor_occ' : vendor_dict}
	return render(request, 'vendz/vendors.html', context)

def vendorDetail(request, vendorID):
	currVendor = get_object_or_404(Vendor,id = vendorID)
	pastEvents = []
	upcomingEvents = []
	events = Event.objects.all()
	for event in events:
		vendors = event.vendors.all()
		for vendor in vendors:
			if (currVendor.id == vendor.id):
				if (event.end_time >= timezone.now()):
					upcomingEvents.append(event);
				else:
					pastEvents.append(event)
	context = {'vendor' : currVendor, 'pastEvents' : pastEvents, 'upcomingEvents' : upcomingEvents, 'occ' : len(pastEvents)}
	return render(request, 'vendz/vendorDetail.html', context)

	

def eventDetail(request, eventID):
	currEvent = get_object_or_404(Event, eventID=eventID) 
	vendor_list = currEvent.vendors.all()
	return render(request, 'vendz/eventDetail.html', {'vendor_list' : vendor_list,'event' : currEvent})


def populateDatabase():
	response = urllib2.urlopen('https://ginger.io/test-project/events/')
	data = json.load(response)
	events = []
	for event in data['data']:
		responseID = urllib2.urlopen('https://ginger.io/test-project/events/' + str(event['id']))
		dataID = json.load(responseID)
		dataID = dataID['data']
		if (Event.objects.filter(eventID = dataID['id'])):
			eventM = Event.objects.get(eventID = dataID['id'])
			eventM.name = dataID['name']
			eventM.start_time = dataID['start_time']
			eventM.end_time = dataID['end_time']
			eventM.timezone = dataID['timezone']
			eventM.location = dataID['location']
			eventM.save()
		else:
			eventM = Event(name = dataID['name'], start_time = dataID['start_time'], end_time = dataID['end_time'], timezone = dataID['timezone'], eventID = dataID['id'], location = dataID['location'])
			eventM.save()
		for vendor in dataID['vendors_list']:
			if (Vendor.objects.filter(name = vendor).exists()):
				eventM.vendors.add(Vendor.objects.get(name = vendor))
			else:
				vendorM = Vendor(name = vendor)
				vendorM.save()
				eventM.vendors.add(vendorM)
			

