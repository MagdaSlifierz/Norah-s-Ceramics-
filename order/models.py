from uuid import uuid4

from django.db import models

from customer.models import AddressDetails, User
from norahs_ceramics.model_mixin import TimestapModel
from product.models import Product


class Order(TimestapModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name="orders",
    )
    status = models.CharField(max_length=300, null=False)
    bill_pence = models.IntegerField()
    transaction_id = models.CharField(max_length=300)
    order_no = models.UUIDField(default=uuid4, editable=False)

    def __str__(self):
        return self.transaction_id


class OrderProduct(TimestapModel):
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        null=False,
        related_name="order_products",
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        related_name="order_products",
    )

    def __str__(self):
        return str(self.product)
