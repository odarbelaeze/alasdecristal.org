from django import forms
from django.forms.models import inlineformset_factory

from .models import Contact
from .models import NewsletterSubscription
from .models import Quote
from .models import QuoteLine


class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ('name', 'email', )


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'subject', 'email', 'phone', 'city', 'message', )


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ('name', 'subject', 'email', 'phone', 'city', )


QuoteLineFormset = inlineformset_factory(
    Quote, QuoteLine, extra=2,
    fields=('product', 'quantity', ))
