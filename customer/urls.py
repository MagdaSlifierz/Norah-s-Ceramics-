from django.urls import path

from customer.views import (
    ChangePasswordView,
    CustomerAddressView,
    CustomerOrderHistoryListView,
    CustomerProfileView,
    DeleteCustomerProfile,
    UserReviewListView,
)

urlpatterns = [
    path(
        "<int:id>",
        CustomerProfileView.as_view(),
        name="customer_profile",
    ),
    path(
        "<int:id>/address",
        CustomerAddressView.as_view(),
        name="customer_address",
    ),
    path(
        "<int:pk>/delete",
        DeleteCustomerProfile.as_view(),
        name="customer_delete",
    ),
    path(
        "<int:pk>/password_change",
        ChangePasswordView.as_view(),
        name="password_change",
    ),
    path(
        "<int:pk>/order_history",
        CustomerOrderHistoryListView.as_view(),
        name="order_history",
    ),
    path(
        "<int:pk>/user_reviews",
        UserReviewListView.as_view(),
        name="user_reviews",
    ),
]
