"""
URL patterns for Home application
"""

from django.urls import path

from policies.views import (
    PrivacyPolicyView,
    ReturnsPolicyView,
    ShippingPolicyView,
    TermsAndConditionsView,
)

urlpatterns = [
    path(
        "terms_and_conditions", TermsAndConditionsView.as_view(), name="terms"
    ),
    path("privacy_policy", PrivacyPolicyView.as_view(), name="privacy_policy"),
    path("returns_policy", ReturnsPolicyView.as_view(), name="returns_policy"),
    path("returns_policy", ReturnsPolicyView.as_view(), name="returns_policy"),
    path(
        "shipping_and_delivery", ShippingPolicyView.as_view(), name="shipping"
    ),
]
