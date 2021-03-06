import datetime
import pytest

from django.core.urlresolvers import reverse


@pytest.fixture
def year():
    today = datetime.date.today()
    return str(today.year)


def test_hit_homepage(client):
    # GIVEN Any state
    # WHEN Someone hits the homepage
    resp = client.get(reverse('home'))
    # THEN They receive a response
    assert 200 == resp.status_code


def test_copyright_years(client, year):
    # GIVEN any state
    # WHEN a user requests a page
    resp = client.get(reverse('home'))
    # THEN the copyright years are right
    assert '2013' in resp.content.decode()
    assert year in resp.content.decode()


def test_hit_products(client):
    # GIVEN Any state
    # WHEN Someone hits the products page
    resp = client.get(reverse('products'))
    # THEN They receive a response
    assert 200 == resp.status_code


def test_hit_about(client):
    # GIVEN Any state
    # WHEN Someone hits the about page
    resp = client.get(reverse('about'))
    # THEN They receive a response
    assert 200 == resp.status_code


def test_hit_agenda(client):
    # GIVEN Any state
    # WHEN Someone hits the agenda page
    resp = client.get(reverse('agenda'))
    # THEN They receive a response
    assert 200 == resp.status_code


def test_hit_contact(client):
    # GIVEN Any state
    # WHEN Someone hits the contact page
    resp = client.get(reverse('contact'))
    # THEN They receive a response
    assert 200 == resp.status_code
