import pytest

from django.core.urlresolvers import reverse
from django.core import mail

from ecommerce.models import Contact
from ecommerce.models import NewsletterSubscription


@pytest.fixture
def contact():
    return {
        'name': 'John Doe',
        'subject': 'Some stuff',
        'email': 'john@doe.com',
        'phone': 'this is totally my phone',
        'city': 'You should not really care',
        'message': 'ICU4CU'
    }


@pytest.fixture
def person(contact):
    _person = contact.copy()
    _person.pop('message')
    return _person


@pytest.mark.django_db
def test_a_contact_form_is_appropiately_handled(client, contact):
    # GIVEN any state
    # WHEN someone sends a contact
    resp = client.post(reverse('contact'), contact)
    # THEN an email is fired to the director
    assert hasattr(mail, 'outbox')
    assert 1 == len(mail.outbox)
    # And a Contact is created in the db
    assert 1 == Contact.objects.count()
    # And the user is redirected to the thanks page
    assert reverse('contact-thanks') in resp.url


def test_a_contact_form_is_appropiately_validated(client, contact):
    # GIVEN an user forgot to type the email into the contact form
    contact.pop('email')
    # WHEN the user sends the contact
    resp = client.post(reverse('contact'), contact)
    # THEN the user is redirected back
    assert 200 == resp.status_code
    # AND errors are included
    assert 'has-error' in resp.content.decode()


@pytest.mark.django_db
def test_newsletter_subscriptions_are_properly_handled(client):
    # GIVEN Any state
    # WHEN someone subscribes to the newsletter
    resp = client.post(reverse('subscription-add'), {
        'name': 'John Doe',
        'email': 'john@doe.com'
    })
    # THEN The user is redirected to the contact thanks page
    assert 302 == resp.status_code
    assert reverse('contact-thanks') == resp.url
    # AND a new subscription is addded to the db
    assert 1 == NewsletterSubscription.objects.count()


@pytest.mark.django_db
def test_newsletter_subscriptions_are_properly_validated(client):
    # GIVEN Any state
    # WHEN someone forgets to fill in the email to the newsletter form
    resp = client.post(reverse('subscription-add'), {
        'name': 'John Doe',
    })
    # THEN The user is redirected back with errors
    assert 200 == resp.status_code
    assert not hasattr(resp, 'url')
