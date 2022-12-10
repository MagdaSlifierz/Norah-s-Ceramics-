import pytest
from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed

from product.tests import factories

PRODUCT_LIST_URL = reverse("product_list")


@pytest.fixture
def sub_category():
    category = factories.CategoryModelFactory()
    sub_category = factories.SubCategoryModelFactory(category=category)
    return sub_category


@pytest.mark.django_db
def test_product_list_use_correct_template(client):
    res = client.get(PRODUCT_LIST_URL)
    assert res.status_code == 200
    assertTemplateUsed(res, "product/product-list.html")


@pytest.mark.django_db
def test_product_list_return_list_of_products(client, sub_category):
    factories.ProductModelFactory.create_batch(4, sub_category=sub_category)
    res = client.get(PRODUCT_LIST_URL)
    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 4


@pytest.mark.django_db
def test_product_list_return_list_is_paginated(client, sub_category):
    factories.ProductModelFactory.create_batch(8, sub_category=sub_category)
    res = client.get(PRODUCT_LIST_URL)
    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 4
    assert res.context_data["is_paginated"] is True
    assert res.context_data["page_obj"].number == 1
    assert str(res.context_data["page_obj"]) == "<Page 1 of 2>"


@pytest.mark.django_db
def test_product_list_return_next_page_content(client, sub_category):
    factories.ProductModelFactory.create_batch(7, sub_category=sub_category)
    res = client.get(f"{PRODUCT_LIST_URL}?page=2")
    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 3
    assert res.context_data["is_paginated"] is True
    assert res.context_data["page_obj"].number == 2
    assert str(res.context_data["page_obj"]) == "<Page 2 of 2>"


@pytest.mark.django_db
def test_product_list_return_only_active_products(client, sub_category):
    factories.ProductModelFactory(sub_category=sub_category)
    factories.ProductModelFactory(is_active=False, sub_category=sub_category)
    res = client.get(f"{PRODUCT_LIST_URL}")
    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 1
    assert res.context_data["object_list"][0].is_active is True
