from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.shortcuts import redirect

from .models import NewsletterSuscription
from .models import Contact
from .models import Quote

from .forms import NewsletterSuscriptionForm
from .forms import ContactForm
from .forms import QuoteForm
from .forms import QuoteLineFormset


class NewsletterSuscriptionCreate(CreateView):
    model = NewsletterSuscription
    form_class = NewsletterSuscriptionForm
    template_name = 'ecommerce/newsletter_form.html'
    success_url = '/ecommerce/contact/thanks/'


class ContactCreate(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact.html'
    success_url = '/ecommerce/contact/thanks/'

    def form_valid(self, form):
        subject = form.cleaned_data['subject']

        lines = [
            'De: %s' % form.cleaned_data['name'],
            'Email: %s' % form.cleaned_data['email'],
            'Teléfono: %s' % form.cleaned_data['phone'],
            'Ciudad: %s' % form.cleaned_data['city'],
            '\nMensaje: \n%s' % form.cleaned_data['message']
        ]

        send_mail(
            subject, '\n'.join(lines),
            'contacto@alasdecristal.org',
            ['direccion@alasdecristal.org']
        )

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
