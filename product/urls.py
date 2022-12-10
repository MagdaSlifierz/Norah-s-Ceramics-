from django.urls import path

from product.views import ProductDetailView, ProductListView, ReviewView

urlpatterns = [
    path("", ProductListView.as_view(), name="product_list"),
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path(
        "<slug:slug>/review",
        ReviewView.as_view(),
        name="review",
    ),
]
