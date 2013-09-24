# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.forms.models import inlineformset_factory

from ecommerce.models import NewsletterSuscription 
from ecommerce.models import Contact
from ecommerce.models import Quote
from ecommerce.models import QuoteLine


class NewsletterSuscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSuscription


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote


QuoteLineFormset = inlineformset_factory(Quote, QuoteLine, extra=2)
