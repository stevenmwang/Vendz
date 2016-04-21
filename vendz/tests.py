from django.test import TestCase
from .models import Vendor, Event
from django.test import Client
# Create your tests here.

class ModelTests(TestCase):
	def test_event_in_past(self):
		pastEvents = []
		upcomingEvents = []
		events = Event.objects.all()
		for event in events:
			vendors = event.vendors.all()
			for vendor in vendors:
				if (vendor.vendor_id == 100):
					if (event.end_time >= timezone.now()):
						upcomingEvents.append(event);
					else:
						pastEvents.append(event)


		self.assertEqual(len(pastEvents), 0);
		self.assertEqual(len(upcomingEvents), 0);

	def test_all_events(self):
		events = Event.objects.all()
		self.assertEqual(len(events), 0)

class InitTest(TestCase):
	def test_vendors(self):
		client = Client()
		response = client.get('vendz/vendors')
		self.assertEqual(response.status_code, 200)

	def test_events(self):
		client = Client();
		response = client.get('vendz/events')
		self.assertEqual(response.status_code, 200)

	def test_specific_event(self):
		client = Client();
		response = client.get('vendz/events/1')
		self.assertEqual(response.status_code, 200)

	def test_specific_vendor(self):
		client = Client();
		response = client.get('vendz/vendors/1')
		self.assertEqual(response.status_code, 200)

	def test_not_event(self):
		client = Client();
		response = client.get('vendz/events/999')
		self.assertEqual(response.status_code, 404)

	def test_not_vendor(self):
		client = Client();
		response = client.get('vendz/vendors/999')
		self.assertEqual(response.status_code, 404)

