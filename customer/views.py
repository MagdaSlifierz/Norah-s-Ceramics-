import sweetify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import DeleteView

from customer.forms import AddressForm, UpdatePersonalInformationForm
from customer.models import User
from order.models import Order
from reviews.models import ProductReview


class CustomerProfileView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"

    def get(self, request: HttpRequest, id: int) -> HttpResponse:
        context = {
            "personal_info_form_errors": request.session.pop(
                "personal_info_form_errors", None
            ),
            "address_form_errors": request.session.pop(
                "address_form_errors", None
            ),
            "personal_information_form": UpdatePersonalInformationForm(
                instance=request.user
            ),
            "address_information_form": AddressForm(
                instance=request.user.address_details
            ),
        }
        return render(request, "customer/customer_profile.html", context)

    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        """Update user information"""
        personal_info_form = UpdatePersonalInformationForm(
            instance=request.user, data=request.POST or None
        )

        if personal_info_form.is_valid() and personal_info_form.has_changed():
            sweetify.toast(
                self.request,
                "your personal information has been updated successfully!",
                position="top",
                timer=3000,
            )
            personal_info_form.save()

        else:
            request.session[
                "personal_info_form_errors"
            ] = personal_info_form.errors

        return HttpResponseRedirect(
            reverse("customer_profile", kwargs={"id": id})
        )


class CustomerAddressView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"

    def post(self, request: HttpRequest, id: int) -> HttpResponse:
        """Update/create customer address details"""
        address_form = AddressForm(
            instance=request.user.address_details, data=request.POST or None
        )
        if address_form.is_valid() and address_form.has_changed():
            address_form.save(commit=True)
            if request.user.address_details_id != address_form.instance.id:
                # Update existed address
                request.user.address_details_id = address_form.instance.id
                request.user.save()
            sweetify.toast(
                self.request,
                "your address information has been updated successfully!",
                position="top",
                timer=3000,
            )
        else:
            request.session["address_form_errors"] = address_form.errors

        return HttpResponseRedirect(
            reverse("customer_profile", kwargs={"id": id})
        )


class DeleteCustomerProfile(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "confirm_delete_profile.html"
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"

    def get_success_url(self):
        sweetify.toast(
            self.request,
            "your account has been deleted successfully",
            icon="info",
        )
        return reverse("home")


class ChangePasswordView(
    LoginRequiredMixin, SuccessMessageMixin, PasswordChangeView
):
    model = User
    template_name = "change_password.html"
    success_message = "your password has been changed successfully"
    success_url = reverse_lazy("home")
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"


class CustomerOrderHistoryListView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"
    model = Order
    paginate_by = 3
    template_name = "customer/customer_orders.html"

    def get_queryset(self) -> QuerySet[Order]:
        """Get customer orders query set"""
        user_order = (
            Order.objects.filter(user=self.request.user)
            .order_by("-created_at")
            .all()
        )
        return user_order

    def get_context_data(self, **kwargs: dict) -> dict:
        """Expand context data with customer order history"""
        context = super().get_context_data(**kwargs)
        orders = self.get_queryset()
        context["orders_data"] = {}
        for order in orders:
            products_with_qty = {}
            for order_product in order.order_products.all():
                if order_product.product_id in products_with_qty:
                    products_with_qty[order_product.product_id]["qty"] += 1
                    products_with_qty[order_product.product_id][
                        "name"
                    ] = order_product.product.name
                else:
                    products_with_qty[order_product.product_id] = {
                        "qty": 1,
                        "name": order_product.product.name,
                    }
            context["orders_data"][order.id] = [
                v for _, v in products_with_qty.items()
            ]

        return context


class UserReviewListView(LoginRequiredMixin, ListView):
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"

    model = ProductReview
    template_name = "customer/customer_reviews.html"
    paginate_by = 2

    def get_queryset(self):
        """Get user review history query set"""
        if self.request.user.is_authenticated:
            user_reviews = (
                ProductReview.objects.filter(reviewer_id=self.request.user.id)
                .order_by("-created_at")
                .all()
            )
            return user_reviews
