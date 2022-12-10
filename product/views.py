import sweetify
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from django.views.generic import DetailView, ListView

from product.forms import FilterForm
from product.models import Color, Product
from reviews.forms import ProductReviewForm
from reviews.models import ProductReview


class ProductListView(ListView):
    model = Product
    paginate_by = 4
    template_name = "product/product-list.html"

    def filter_products(
        self, product_query: QuerySet[Product]
    ) -> QuerySet[Product]:
        """Filter products by category, sub_category, and min & max price"""
        min_price = self.request.GET.get("min_price")
        max_price = self.request.GET.get("max_price")
        if sub_category := self.request.GET.get("sub_category"):
            product_query = product_query.filter(
                sub_category__name=sub_category
            )
        if category := self.request.GET.get("category"):
            product_query = product_query.filter(
                sub_category__category_id=category
            )
        if min_price and max_price:
            product_query = product_query.filter(
                price_pence__range=(
                    self._to_pence(int(min_price)),
                    self._to_pence(int(max_price)),
                )
            )
        return product_query

    def filter_products_colors(
        self, product_query: QuerySet[Product]
    ) -> QuerySet[Product]:
        """Filter products by colors"""
        colors = Color.objects.all()
        color_filters = []

        for color in colors:
            if color.name in self.request.GET:
                color_filters.append(Q(colors=color.name))
        if color_filters:
            color_query = color_filters.pop()
            for filter in color_filters:
                color_query |= filter
            product_query = product_query.filter(color_query)
        return product_query

    def sort_products(
        self, product_query: QuerySet[Product]
    ) -> QuerySet[Product]:
        """Sort products by name or price"""
        if sort_by := self.request.GET.get("sort_by"):
            if sort_by == "name_asc":
                product_query = product_query.order_by("name").distinct("name")
            if sort_by == "name_desc":
                product_query = product_query.order_by("-name").distinct(
                    "name"
                )
            if sort_by == "price_asc":
                product_query = product_query.order_by("price_pence").distinct(
                    "price_pence"
                )
            if sort_by == "price_desc":
                product_query = product_query.order_by(
                    "-price_pence"
                ).distinct("price_pence")
        return product_query

    def get_queryset(self) -> QuerySet[Product]:
        """Get filtered and sorted products"""
        product_query = Product.objects.filter(is_active=True).all()
        product_query = self.filter_products(product_query)
        product_query = self.filter_products_colors(product_query)
        product_query = self.sort_products(product_query)
        return product_query.distinct("id", "name", "price_pence")

    def get_context_data(self, **kwargs):
        """Expand context with extra data for search urls. They are used to
        preserve user search"""
        context = super().get_context_data(**kwargs)
        query_params = ""
        if sub_category := self.request.GET.get("sub_category"):
            query_params += f"sub_category={sub_category}&"
        if category := self.request.GET.get("category"):
            query_params += f"category={category}&"
        if min_price := self.request.GET.get("min_price"):
            query_params += f"min_price={min_price}&"
        if max_price := self.request.GET.get("max_price"):
            query_params += f"max_price={max_price}&"
        if sort_by := self.request.GET.get("sort_by"):
            query_params += f"sort_by={sort_by}&"

        initials = {
            "category": category,
            "sub_category": sub_category,
            "min_price": min_price,
            "max_price": max_price,
        }
        context["initial_colors"] = []
        colors = Color.objects.all()
        for color in colors:
            if color.name in self.request.GET:
                query_params += f"{color.name}=on&"
                context["initial_colors"].append(color.name)
        context["query_params"] = query_params
        context["filter_form"] = FilterForm(initial=initials)
        return context

    @staticmethod
    def _to_pence(price: int) -> int:
        return price * 100


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/product-details.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        """Expand context with product review data"""
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context["review_form"] = ProductReviewForm()
        context["reviews"] = ProductReview.objects.filter(
            product_id=self.object.id, is_admin_approved=True, is_visible=True
        ).all()
        return context


class ReviewView(LoginRequiredMixin, View):
    login_url = "/accounts/login/"
    redirect_field_name = "account_login"

    def post(self, request: HttpRequest, slug: str) -> HttpResponse:
        """Create product review"""
        product = get_object_or_404(Product, slug=slug)
        product_review = ProductReview.objects.filter(
            product_id=product.id, reviewer_id=request.user.id
        ).first()
        if product_review:
            messages.error(
                request, "You have already given review to this product !"
            )
            return HttpResponseRedirect(
                reverse("product_detail", kwargs={"slug": slug})
            )
        else:
            review_form = ProductReviewForm(data=request.POST or None)
            if review_form.is_valid():
                review_form.instance.product_id = product.id
                review_form.instance.reviewer_id = request.user.id
                review_form.instance.save()
                messages.success(
                    request,
                    "Thank you for your review! Your review will be"
                    " visible after approval by the website administrator",
                )

        return HttpResponseRedirect(
            reverse("product_detail", kwargs={"slug": slug})
        )
