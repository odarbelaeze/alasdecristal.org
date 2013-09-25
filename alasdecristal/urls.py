from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from alasdecristal.views import *
from ecommerce.views     import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'alasdecristal.views.home', name='home'),
    # url(r'^alasdecristal/', include('alasdecristal.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    # My urls

    # Base views
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^agenda/$', AgendaView.as_view(), name='agenda'),
    url(r'^contact/$', ContactCreate.as_view(), name='contact'),

    # Ecommerce views
    url(r'^ecommerce/suscription/add/$', NewsletterSuscriptionCreate.as_view(), name='suscription-add'),
    # url(r'^ecommerce/contact/add/$', ContactCreate.as_view(), name='contact-add'),
    url(r'^ecommerce/contact/thanks/$', ContactThanks.as_view(), name='contact-thanks'),
    url(r'^ecommerce/quote/add/$', QuoteCreate.as_view(), name='quote-add'),

    # Third party app urls

)
