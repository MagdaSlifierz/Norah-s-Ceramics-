from collections import namedtuple
from uuid import UUID, uuid4

from django.db import models
from django.http import HttpRequest

from customer.models import User
from norahs_ceramics.model_mixin import TimestapModel
from product.models import Product

BasketSummary = namedtuple(
    "BasketSummary",
    ["total_qty", "total_price", "sorted_products", "vat_amount"],
)


class Basket(TimestapModel):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    customer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="customer", null=True
    )

    def add_product(self, product_id: int) -> None:
        """Add basket product to the basket"""
        basket_product = BasketProduct(
            product_id=product_id, basket_id=self.id
        )
        basket_product.save()

    def subtract_product(self, product_id: int) -> None:
        """Remove basket product from the basket"""
        basket_product = BasketProduct.objects.filter(
            product_id=product_id, basket_id=self.id
        ).first()
        if basket_product:
            basket_product.delete()

    def delete_product(self, product_id: int) -> None:
        """Delete all basket products of given id from the basket"""
        basket_products = BasketProduct.objects.filter(
            product_id=product_id, basket_id=self.id
        ).all()

        if basket_products:
            basket_products.all().delete()

    def total_basket_price(self) -> int:
        """Calculate total basket price in pence"""
        basket_products = BasketProduct.objects.filter(basket_id=self.id).all()
        total_price_pence = 0
        for basket_product in basket_products:
            total_price_pence += basket_product.product.price_pence
        return total_price_pence

    def total_basket_products_qty(self) -> int:
        """Return total number of products in the basket"""
        basket_products = BasketProduct.objects.filter(basket_id=self.id).all()
        return len(basket_products)

    @classmethod
    def get_or_create_basket_with_id(cls, id: str | UUID) -> "Basket":
        """Get basket with given id or create one"""
        basket = cls.objects.filter(id=id).first()
        if not basket:
            basket = cls(id=id)
            basket.save()
        return basket

    @classmethod
    def get_basket(cls, request: HttpRequest) -> "Basket":
        """Get basket for user. There can be 3 scenarios:
        1. if user is authenticated then try to get one from DB or create new
        2. when user is not authenticated try to get basket from session
           basket id
        3. If user is not authenticated and there is no basket id in session
           then create new and save it in the session
        """
        session_basket_id = request.session.get("basket_id")
        if request.user.is_authenticated:
            basket = request.user.get_user_basket()
            if not basket:
                if session_basket_id:
                    basket = cls.get_or_create_basket_with_id(
                        session_basket_id
                    )
                    basket.customer_id = request.user.id
                    basket.save()
                else:
                    basket = request.user.create_user_basket()
        elif session_basket_id:
            basket = cls.objects.filter(id=session_basket_id).first()
            if not basket:
                basket = cls()
                basket.save()
            request.session["basket_id"] = str(basket.id)
        else:
            basket = cls()
            basket.save()
            request.session["basket_id"] = str(basket.id)
        return basket

    def basket_summary(self) -> BasketSummary:
        """Gets basket summary that contains all details that are required to
        display the basket"""
        if self.basket_products:
            basket_products = self.basket_products.all()
        else:
            basket_products = []

        products_with_qty = {}

        for basket_product in basket_products:
            if basket_product.product_id in products_with_qty:
                products_with_qty[basket_product.product_id]["qty"] += 1
                products_with_qty[basket_product.product_id][
                    "total_product_price"
                ] = (
                    basket_product.product.price_pence
                    * products_with_qty[basket_product.product_id]["qty"]
                )
            else:
                products_with_qty[basket_product.product_id] = {
                    "product": basket_product.product,
                    "total_product_price": basket_product.product.price_pence,
                    "qty": 1,
                }
        sorted_products = sorted(
            list(products_with_qty.values()), key=lambda x: x["product"].name
        )
        total_qty = self.total_basket_products_qty()
        total_price = self.total_basket_price()
        vat_amount = total_price * 0.2
        basket_summary = BasketSummary(
            total_price=total_price,
            total_qty=total_qty,
            sorted_products=sorted_products,
            vat_amount=vat_amount,
        )
        return basket_summary


class BasketProduct(TimestapModel):
    basket = models.ForeignKey(
        Basket,
        on_delete=models.CASCADE,
        related_name="basket_products",
        null=False,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name="basket_products",
        null=False,
    )
