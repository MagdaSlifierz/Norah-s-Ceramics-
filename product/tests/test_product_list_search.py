import pytest
from django.urls import reverse

from product.tests import factories

PRODUCT_LIST_URL = reverse("product_list")


@pytest.fixture
def sub_category():
    category = factories.CategoryModelFactory()
    sub_category = factories.SubCategoryModelFactory(category=category)
    return sub_category


@pytest.mark.django_db
def test_product_list_search_price_range(client, sub_category):
    expected_product = factories.ProductModelFactory(
        price_pence=1500, sub_category=sub_category
    )
    factories.ProductModelFactory(price_pence=2500, sub_category=sub_category)
    factories.ProductModelFactory(price_pence=500, sub_category=sub_category)
    res = client.get(f"{PRODUCT_LIST_URL}?min_price=10&max_price=20")

    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 1
    assert res.context_data["object_list"][0] == expected_product


@pytest.mark.django_db
def test_product_list_search_sub_category(client):
    category = factories.CategoryModelFactory()
    plates_sub_category = factories.SubCategoryModelFactory(
        name="plates", category=category
    )
    mugs_sub_category = factories.SubCategoryModelFactory(
        name="mugs", category=category
    )
    expected_product = factories.ProductModelFactory(
        sub_category=plates_sub_category
    )
    factories.ProductModelFactory(sub_category=mugs_sub_category)
    res = client.get(f"{PRODUCT_LIST_URL}?sub_category=plates")

    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 1
    assert res.context_data["object_list"][0] == expected_product


@pytest.mark.django_db
def test_product_list_search_category(client):
    ceramics_category = factories.CategoryModelFactory(name="ceramics")
    glass_category = factories.CategoryModelFactory(name="glass")
    plates_sub_category = factories.SubCategoryModelFactory(
        name="plates", category=ceramics_category
    )
    decor_sub_category = factories.SubCategoryModelFactory(
        name="decor", category=glass_category
    )
    expected_product = factories.ProductModelFactory(
        sub_category=plates_sub_category
    )
    factories.ProductModelFactory(sub_category=decor_sub_category)
    res = client.get(f"{PRODUCT_LIST_URL}?category=ceramics")

    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 1
    assert res.context_data["object_list"][0] == expected_product


@pytest.mark.django_db
def test_product_list_search_colors(client, sub_category):
    color_blue = factories.ColorModelFactory(name="blue")
    color_white = factories.ColorModelFactory(name="white")
    color_black = factories.ColorModelFactory(name="black")
    expected_product = factories.ProductModelFactory(
        sub_category=sub_category, colors=(color_blue, color_white)
    )
    factories.ProductModelFactory(
        sub_category=sub_category, colors=(color_black,)
    )
    res = client.get(f"{PRODUCT_LIST_URL}?blue=on&white=on")

    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 1
    assert res.context_data["object_list"][0] == expected_product


@pytest.mark.django_db
@pytest.mark.parametrize(
    ["sort_by", "expected_names"],
    [
        ("name_asc", ("a", "z")),
        ("name_desc", ("z", "a")),
        ("price_asc", ("a", "z")),
        ("price_desc", ("z", "a")),
    ],
)
def test_product_list_search_sort_by_asc(
    client, sub_category, sort_by, expected_names
):
    factories.ProductModelFactory(
        name="a", sub_category=sub_category, price_pence=1000
    )
    factories.ProductModelFactory(
        name="z", sub_category=sub_category, price_pence=2000
    )
    res = client.get(f"{PRODUCT_LIST_URL}?sort_by={sort_by}")

    assert res.status_code == 200
    assert len(res.context_data["object_list"]) == 2
    assert res.context_data["object_list"][0].name == expected_names[0]
    assert res.context_data["object_list"][1].name == expected_names[1]


@pytest.mark.django_db
def test_product_list_search_context_return_query_params(client):
    factories.ColorModelFactory(name="blue")
    query_params = (
        "sub_category=mugs&category=ceramics&min_price=10&"
        "max_price=20&sort_by=price_desc&blue=on&"
    )
    res = client.get(f"{PRODUCT_LIST_URL}?{query_params}")
    assert res.status_code == 200
    assert res.context_data["query_params"] == query_params
