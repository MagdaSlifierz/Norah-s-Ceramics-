import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from customer.forms import UpdatePersonalInformationForm
from product.tests import factories


def get_customer_profile_url(id=1):
    return reverse("customer_profile", kwargs={"id": id})


@pytest.mark.django_db
def test_customer_profile_use_correct_template(client, django_user_model):
    user = django_user_model.objects.create_user(
        username="user1", password="bar"
    )
    client.force_login(user)
    res = client.get(get_customer_profile_url(id=1))
    assert res.status_code == 200
    assertTemplateUsed(res, "customer/customer_profile.html")


@pytest.mark.django_db
def test_happy_flow_personal_info_form():
    form_data = {
        "phone_number": "07869741585",
        "first_name": "Mary",
        "last_name": "Thompson",
        "email": "mary88@gmail.com",
    }
    personal_info_form = UpdatePersonalInformationForm(data=form_data)
    assert personal_info_form.is_valid()


@pytest.mark.django_db
def test_required_data_missing_in_personal_info_form():
    personal_info_form = UpdatePersonalInformationForm(data={})
    assert not personal_info_form.is_valid()
