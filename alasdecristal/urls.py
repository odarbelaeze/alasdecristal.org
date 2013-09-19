from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from alasdecristal.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alasdecristal.views.home', name='home'),
    # url(r'^alasdecristal/', include('alasdecristal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # My urls

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^agenda/$', AgendaView.as_view(), name='agenda'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),

    # Third party app urls

)
