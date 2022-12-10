import factory

from product import models


class CategoryModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Category

    name = "ceramics"


class SubCategoryModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.SubCategory

    name = "mugs"


class ColorModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Color

    name = "red"


class ProductModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Product

    name = "Grey Mug"
    slug = factory.Sequence(lambda x: f"grey_mug_{x+1}")
    price_pence = 2000
    description = "Just a mug"
    short_description = "Just a..."
    is_active = True
    is_featured = True
    width_cm = 8
    height_cm = 10
    length_cm = 7
    volume_ml = 500
    sub_category = factory.SubFactory(SubCategoryModelFactory)

    @factory.post_generation
    def colors(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for color in extracted:
                self.colors.add(color)
