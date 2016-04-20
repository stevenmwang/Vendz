from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/$', views.events, name = 'events'),
    url(r'^events/(?P<eventID>[0-9]+)/$', views.eventDetail, name='Event Detail'),
    url(r'^vendors/$', views.vendors.as_view(), name = 'vendors'),
    url(r'^vendors/(?P<vendorID>[0-9]+)/$', views.vendorDetail, name='Vendor Detail'),

]