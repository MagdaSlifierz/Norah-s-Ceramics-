from django.urls import path

from checkout import views

urlpatterns = [
    path("", views.OrderSummaryView.as_view(), name="checkout"),
    path(
        "create_checkout_session/",
        views.create_checkout_session,
        name="checkout_session",
    ),
    path("success/<str:session_id>", views.SuccessView.as_view()),  # new
    path("cancel/", views.CancelledView.as_view()),  # new # new
    # new # new
]
