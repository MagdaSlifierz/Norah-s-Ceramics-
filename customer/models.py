from __future__ import annotations

from typing import TYPE_CHECKING

from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from norahs_ceramics.model_mixin import TimestapModel

if TYPE_CHECKING:
    from basket.models import Basket


class User(AbstractUser):
    phone_number = PhoneNumberField(null=True, blank=False, unique=True)
    address_details = models.OneToOneField(
        "AddressDetails", null=True, on_delete=models.CASCADE
    )

    def get_user_basket(self) -> Basket:
        """Get assigned basket to customer or None"""
        from basket.models import Basket

        user_basket = (
            Basket.objects.filter(customer_id=self.id)
            .order_by("-created_at")
            .first()
        )
        return user_basket

    def create_user_basket(self) -> Basket:
        """Create an empty basket for user"""
        from basket.models import Basket

        return Basket.objects.create(customer_id=self.id)


class AddressDetails(TimestapModel):
    address_1 = models.CharField(
        verbose_name="Address", max_length=100, default=""
    )
    address_2 = models.CharField(
        verbose_name="Address 1", max_length=100, default=""
    )

    town = models.CharField(
        verbose_name="Town/City", max_length=100, default=""
    )
    postcode = models.CharField(
        verbose_name="Post Code", max_length=8, default=""
    )
    county = models.CharField(
        verbose_name="County", max_length=100, default=""
    )
    country = models.CharField(
        verbose_name="Country", max_length=100, default=""
    )
