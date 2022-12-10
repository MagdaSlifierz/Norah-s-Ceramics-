import pytest

from basket.models import BasketProduct
from basket.tests import factories
from product.tests.factories import (
    CategoryModelFactory,
    ProductModelFactory,
    SubCategoryModelFactory,
)


@pytest.fixture
def sub_category():
    category = CategoryModelFactory()
    sub_category = SubCategoryModelFactory(category=category)
    return sub_category


@pytest.mark.django_db
def test_add_product_method(sub_category):
    basket = factories.BasketModelFactory()
    product = ProductModelFactory(sub_category=sub_category)
    basket.add_product(product.id)
    basket_products = BasketProduct.objects.all()
    assert len(basket_products) == 1
    assert str(basket_products[0].basket_id) == basket.id
    assert basket_products[0].product_id == product.id


@pytest.mark.django_db
def test_subtract_product_method(sub_category):
    basket = factories.BasketModelFactory()
    product = ProductModelFactory(sub_category=sub_category)
    BasketProduct(product_id=product.id, basket_id=basket.id).save()
    basket.subtract_product(product.id)
    basket_products = BasketProduct.objects.all()
    assert len(basket_products) == 0


@pytest.mark.django_db
def test_delete_product_method(sub_category):
    basket = factories.BasketModelFactory()
    products = ProductModelFactory.create_batch(2, sub_category=sub_category)
    factories.BasketProductModelFactory.create_batch(
        4, product_id=products[0].id, basket_id=basket.id
    )
    factories.BasketProductModelFactory.create_batch(
        4, product_id=products[1].id, basket_id=basket.id
    )
    basket_products = BasketProduct.objects.all()
    assert len(basket_products) == 8
    basket.delete_product(products[0].id)
    basket_products = BasketProduct.objects.all()
    assert len(basket_products) == 4


@pytest.mark.django_db
def test_total_basket_price_method(sub_category):
    basket = factories.BasketModelFactory()
    product = ProductModelFactory(sub_category=sub_category)
    factories.BasketProductModelFactory.create_batch(
        4, product_id=product.id, basket_id=basket.id
    )
    total_price_pence = basket.total_basket_price()
    assert total_price_pence == 8000
