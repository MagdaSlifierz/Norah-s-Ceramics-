import sweetify
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from basket.models import Basket


class BasketView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {}
        basket = Basket.get_basket(request)
        basket_summary = basket.basket_summary()
        context = {
            "basket_products": basket_summary.sorted_products,
            "sum_products_qty": basket_summary.total_qty,
            "total_basket_price": basket.total_basket_price,
        }
        return render(request, "basket/basket.html", context)


class AddToBasketView(View):
    def post(self, request: HttpRequest, product_id: int) -> HttpResponse:
        basket = Basket.get_basket(request)
        basket.add_product(product_id=product_id)
        sweetify.toast(
            self.request,
            "the product has been successfully added to the basket",
            timer=2500,
            position="top",
        )
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class SubtractFromBasketView(View):
    def post(self, request: HttpRequest, product_id: int) -> HttpResponse:
        basket = Basket.get_basket(request)
        basket.subtract_product(product_id=product_id)
        sweetify.toast(
            self.request,
            "the product has been successfully removed from the basket",
            timer=2500,
            position="top",
        )
        return HttpResponseRedirect(reverse("basket"))


class DeleteFromBasketView(View):
    def post(self, request: HttpRequest, product_id: int) -> HttpResponse:
        basket = Basket.get_basket(request)
        basket.delete_product(product_id=product_id)
        sweetify.toast(
            self.request,
            "the products has been successfully removed from the basket",
            timer=2500,
            position="top",
        )
        return HttpResponseRedirect(reverse("basket"))
