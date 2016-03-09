from django.conf.urls import include
from django.conf.urls import url

from alasdecristal.views import AboutView
from alasdecristal.views import AgendaView
from alasdecristal.views import ContactView
from alasdecristal.views import HomeView
from alasdecristal.views import ProductsView

from ecommerce.views import ContactThanks
from ecommerce.views import NewsletterSuscriptionCreate
from ecommerce.views import QuoteCreate

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^products/$', ProductsView.as_view(), name='products'),
    url(r'^about/$', AboutView.as_view(), name='about'),
    url(r'^agenda/$', AgendaView.as_view(), name='agenda'),
    url(r'^contact/$', ContactView.as_view(), name='contact'),

    # Ecommerce views
    url(r'^ecommerce/suscription/add/$',
        NewsletterSuscriptionCreate.as_view(), name='suscription-add'),
    url(r'^ecommerce/contact/thanks/$',
        ContactThanks.as_view(), name='contact-thanks'),
    url(r'^ecommerce/quote/add/$',
        QuoteCreate.as_view(), name='quote-add'),
]
