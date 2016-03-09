import json
import os

from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic import View


def bucketize(iterable, count):
    bucket = []
    while len(iterable):
        temp = []
        for x in range(count):
            temp.append(iterable.pop())
            if not len(iterable):
                break
        bucket.append(temp)
    return bucket


class FooterFormMixin(View):
    """docstring for FooterFormMixin"""
    def __init__(self):
        super().__init__()


class HomeView(FooterFormMixin, TemplateView):
    template_name = 'index.html'


class ProductsView(FooterFormMixin, TemplateView):
    template_name = 'products.html'
    feature_fixture = os.path.join(
        settings.PROJECT_ROOT, 'webapp/dist/data/featured.json')
    product_fixture = os.path.join(
        settings.PROJECT_ROOT, 'webapp/dist/data/products.json')

    def get_context_data(self, **kwargs):
        context = super(ProductsView, self).get_context_data(**kwargs)

        f = open(self.feature_fixture)
        featured = json.load(f)
        f.close()
        context['featured'] = bucketize(featured, 3)

        f = open(self.product_fixture)
        products = json.load(f)
        f.close()
        context['products'] = bucketize(products, 3)

        return context


class AboutView(FooterFormMixin, TemplateView):
    template_name = 'about.html'
    team_fixture = os.path.join(
        settings.PROJECT_ROOT, 'webapp/dist/data/team.json')

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)

        f = open(self.team_fixture)
        teams = json.load(f)
        f.close()
        context['teams'] = teams

        return context


class AgendaView(FooterFormMixin, TemplateView):
    template_name = 'agenda.html'
    agenda_fixture = os.path.join(
        settings.PROJECT_ROOT, 'webapp/dist/data/hints.json')

    def get_context_data(self, **kwargs):
        context = super(AgendaView, self).get_context_data(**kwargs)

        f = open(self.agenda_fixture)
        hints = json.load(f)
        f.close()
        context['hints'] = hints

        return context


class ContactView(FooterFormMixin, TemplateView):
    template_name = 'contact.html'
