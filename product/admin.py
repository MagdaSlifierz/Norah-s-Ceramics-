from django.contrib import admin

from product.models import Category, Color, Product, SubCategory


class ProductAdmin(admin.ModelAdmin):
    """
    Admin setting to display list of products
    """

    model = Product
    list_display = (
        "name",
        "slug",
        "price_pence",
        "description",
        "short_description",
        "is_active",
        "width_cm",
        "height_cm",
        "length_cm",
        "volume_ml",
        "sub_category",
        "image",
    )


class ProductSubCategoryAdmin(admin.ModelAdmin):
    """
    Admin setting to display product subcategory
    """

    model = SubCategory
    list_display = (
        "name",
        "category",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(SubCategory, ProductSubCategoryAdmin)
admin.site.register(Color)
