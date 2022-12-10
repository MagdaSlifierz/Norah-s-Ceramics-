import factory

from basket import models


class BasketModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Basket

    id = "63b79767-a4fb-4207-8140-e8416a9832ff"
    customer_id = None


class BasketProductModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.BasketProduct

    basket_id = "63b79767-a4fb-4207-8140-e8416a9832ff"
    product_id = 1
