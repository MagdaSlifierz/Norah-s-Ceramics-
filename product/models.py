from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from norahs_ceramics.fields import CaseInsensitiveCharField
from norahs_ceramics.model_mixin import TimestapModel


class Category(TimestapModel):
    name = models.CharField(max_length=30, primary_key=True)

    def __str__(self) -> str:
        return self.name


class SubCategory(TimestapModel):
    name = models.CharField(max_length=30, primary_key=True)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="parent_category"
    )

    def __str__(self) -> str:
        return self.name


class Color(TimestapModel):
    name = models.CharField(max_length=30, primary_key=True, unique=True)

    def __str__(self) -> str:
        return self.name


class Product(TimestapModel):
    name = CaseInsensitiveCharField(max_length=100)
    slug = CaseInsensitiveCharField(max_length=200, unique=True)
    price_pence = models.IntegerField(
        null=False, validators=[MaxValueValidator(15000), MinValueValidator(1)]
    )
    description = models.TextField(max_length=2000)
    short_description = models.TextField(max_length=300)
    is_active = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    width_cm = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
    )
    height_cm = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
    )
    length_cm = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
    )
    volume_ml = models.PositiveIntegerField(
        null=True,
        blank=True,
        validators=[MinValueValidator(1)],
    )
    sub_category = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, related_name="sub_category"
    )
    colors = models.ManyToManyField(Color, null=True)

    def validate_image(self) -> None:
        """Validate product image. Raises ValidationError if image is
        too big"""
        # https://stackoverflow.com/questions/6195478/max-image-size-on-file-upload
        filesize = self.file.size
        megabyte_limit = 0.4
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError(
                "Image is too big. Max file size is %sMB" % str(megabyte_limit)
            )

    image = models.ImageField(
        upload_to="product_images/",
        null=True,
        blank=True,
        validators=[validate_image],
    )

    def get_absolute_url(self) -> str:
        return f"/products/{self.slug}/"

    @property
    def reviews_rating(self) -> tuple[float, int]:
        """Return user average reviews rating

        Returns:
            tuple[float, int]: Average rating and number of reviews
        """
        reviews = self.product_reviews.filter(
            is_admin_approved=True, is_visible=True
        )
        ratings = [i.stars for i in reviews]
        try:
            avg_rating = round(sum(ratings) / len(reviews))
        except ZeroDivisionError:
            avg_rating = 0
        return avg_rating, len(reviews)

    def __str__(self) -> str:
        return self.name
