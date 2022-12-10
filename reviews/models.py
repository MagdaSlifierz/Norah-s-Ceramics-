from django.db import models

from customer.models import User
from norahs_ceramics.model_mixin import TimestapModel
from product.models import Product


class ProductReview(TimestapModel):
    TYPE_SELECT = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        null=False,
        related_name="product_reviews",
    )
    reviewer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=False,
        related_name="product_reviews",
    )
    description = models.TextField(blank=False, null=False, default="")
    stars = models.IntegerField(choices=TYPE_SELECT, blank=False, null=False)
    is_visible = models.BooleanField(null=False, default=False)
    is_admin_approved = models.BooleanField(null=False, default=False)
