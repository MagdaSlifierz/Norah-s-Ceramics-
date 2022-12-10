import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from customer.forms import AddressForm
from product.tests import factories


def get_customer_address_url(id=1):
    return reverse("customer_address", kwargs={"id": id})


@pytest.mark.django_db
def test_happy_flow_customer_address_form():
    form_data = {
        "address_1": "9",
        "address_2": "Hathaway Close",
        "town": "Bromley",
        "postcode": "BR2 8RD",
        "county": "Greater London",
        "country": "Great Britain",
    }
    address_form = AddressForm(data=form_data)
    assert address_form.is_valid()


@pytest.mark.django_db
def test_required_data_missing_in_customer_address_form():
    address_form = AddressForm(data={})
    assert not address_form.is_valid()
