# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import View
from django.views.generic import TemplateView

from django.conf import settings

import json
import os

def bucketize(iterable, count):
    bucket = []
    while len(iterable):
        temp = []
        for x in xrange(count):
            temp.append(iterable.pop())
            if not len(iterable):
                break
        bucket.append(temp)
    return bucket

class FooterFormMixin(View):
    """docstring for FooterFormMixin"""
    def __init__(self):
        super(FooterFormMixin, self).__init__()

class HomeView(FooterFormMixin, TemplateView):
    template_name = 'index.html'

class ProductsView(FooterFormMixin, TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)
        
        f = open(os.path.join(settings.PROJECT_ROOT, 'webapp/dist/data/featured.json'))
        featured = json.load(f)
        f.close()
        context['featured'] = bucketize(featured, 3)
        print context['featured']

        f = open(os.path.join(settings.PROJECT_ROOT, 'webapp/dist/data/products.json'))
        products = json.load(f)
        f.close()
        context['products'] = bucketize(products, 3)

        return context

class AboutView(FooterFormMixin, TemplateView):
    template_name = 'about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        f = open(os.path.join(settings.PROJECT_ROOT, 'webapp/dist/data/team.json'))
        teams = json.load(f)
        f.close()
        context['teams'] = teams

        return context

class AgendaView(FooterFormMixin, TemplateView):
    template_name = 'agenda.html'

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)

        f = open(os.path.join(settings.PROJECT_ROOT, 'webapp/dist/data/hints.json'))
        hints = json.load(f)
        f.close()
        context['hints'] = hints

        return context

class ContactView(FooterFormMixin, TemplateView):
    template_name = 'contact.html'
