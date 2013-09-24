# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect

from ecommerce.models import NewsletterSuscription 
from ecommerce.models import Contact
from ecommerce.models import Quote

from ecommerce.forms import *


class NewsletterSuscriptionCreate(CreateView):
    model = NewsletterSuscription
    form_class = NewsletterSuscriptionForm


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/ecommerce/contact/thanks/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']

        message  = 'De: %s \n' % form.cleaned_data['name']
        message += 'Email: %s \n' % form.cleaned_data['email']
        message += 'Teléfono: %s \n' % form.cleaned_data['phone']
        message += 'Ciudad: %s \n' % form.cleaned_data['city']
        message += '\nMensaje: \n%s\n' % form.cleaned_data['message']

        res = send_mail(subject, message, 'contacto@alasdecristal.org', ['contacto@alasdecristal.org'])

        return super(ContactCreate, self).form_valid(form)


class QuoteCreate(CreateView):
    model = Quote
    form_class = QuoteForm
    success_url = '/ecommerce/contact/thanks/'

    def get_context_data(self, **kwargs):
        context = super(QuoteCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            context['quoteline_formset'] = QuoteLineFormset(self.request.POST)
        else:
            context['quoteline_formset'] = QuoteLineFormset()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        quoteline_formset = context['quoteline_formset']
        if quoteline_formset.is_valid():
            self.object = form.save()
            quoteline_formset.instance = self.object
            quoteline_formset.save()
            return redirect(self.get_success_url())
        else:
            return super(QuoteCreate, self).form_invalid(form)


class ContactThanks(TemplateView):
    template_name = 'ecommerce/thanks.html'
