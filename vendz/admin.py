from django.contrib import admin

# Register your models here.
from .models import Event, Vendor

admin.site.register(Event)
admin.site.register(Vendor)