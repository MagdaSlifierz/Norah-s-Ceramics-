"""
URL patterns for Home application
"""

from django.urls import path

from contact.views import ContactView

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
]
