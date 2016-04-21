from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Event, Vendor
from django.core.urlresolvers import reverse
from django.views import generic
from datetime import datetime
from django.utils import timezone



def index(request):
	return render(request, 'vendz/index.html')

def events(request):
	upcomingEvents = Event.objects.filter(end_time__gt=datetime.now()) 
	pastEvents = Event.objects.filter(end_time__lt=datetime.now()) 
	context = {'upcomingEvents' : upcomingEvents, 
				'pastEvents' : pastEvents}
	return render(request, 'vendz/events.html', context)

class vendors(generic.ListView):
	template_name = 'vendz/vendors.html'
	context_object_name = 'vendor_list'
	def get_queryset(self):
		return Vendor.objects.order_by('-occurances')

def vendorDetail(request, vendorID):
	currVendor = get_object_or_404(Vendor,vendor_id = vendorID)
	pastEvents = []
	upcomingEvents = []
	events = Event.objects.all()
	for event in events:
		vendors = event.vendors.all()
		for vendor in vendors:
			if (currVendor.vendor_id == vendor.vendor_id):
				if (event.end_time >= timezone.now()):
					upcomingEvents.append(event);
				else:
					pastEvents.append(event)
	context = {'vendor' : currVendor, 'pastEvents' : pastEvents, 'upcomingEvents' : upcomingEvents}
	return render(request, 'vendz/vendorDetail.html', context)

	

def eventDetail(request, eventID):
	currEvent = get_object_or_404(Event, eventID=eventID) 
	vendor_list = currEvent.vendors.all()
	return render(request, 'vendz/eventDetail.html', {'vendor_list' : vendor_list,'event' : currEvent})


