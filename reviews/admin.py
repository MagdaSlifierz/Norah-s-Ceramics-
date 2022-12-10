from django.contrib import admin

from reviews.models import ProductReview


class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [
        "description",
        "stars",
        "created_at",
        "is_visible",
        "is_admin_approved",
    ]


admin.site.register(ProductReview, ProductReviewAdmin)
