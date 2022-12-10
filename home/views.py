import datetime

from django.contrib import messages
from django.db.models import Count
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.views import View
from django.views.generic import TemplateView

from newsletter.forms import NewsletterUserForm
from newsletter.mailchimp_utils import subscribe
from newsletter.models import NewsletterUser
from order.models import OrderProduct
from product.models import Product


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs: dict) -> dict:
        """Expand context data"""
        context = super().get_context_data(**kwargs)

        context["new_arrivals"] = Product.objects.all().order_by(
            "-created_at"
        )[:10]

        distinct_products = OrderProduct.objects.distinct("product_id")

        context["best_sellers"] = (
            OrderProduct.objects.annotate(count=Count("product_id"))
            .filter(id__in=distinct_products)
            .order_by("-count")[:6]
        )

        context["newsletter_email"] = NewsletterUserForm()
        return context


class NewsletterView(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        """Subscribe email address"""
        email_form = NewsletterUserForm(data=request.POST or None)
        if email_form.is_valid():
            email = email_form.cleaned_data["newsletter_email"]
            newsletter = NewsletterUser.objects.filter(email=email).first()
            if newsletter:
                newsletter.subscribe()
            else:
                data = NewsletterUser()
                data.email = email
                data.created_at = datetime.datetime.now(tz=timezone.utc)
                data.save()
            subscribe(email)
            messages.success(
                request,
                (
                    "Thank you for subscribe to our newsletter!"
                    " You will soon receive a notification on your e-mail."
                ),
            )
            return HttpResponseRedirect(reverse("home"))
        else:
            display_key_map = {
                "newsletter_email": "Newsletter Email",
            }
            for key, value in email_form.errors.items():
                display_key = display_key_map.get(key) or key
                messages.error(request, f"{display_key}: {value[0]}")

        return HttpResponseRedirect(reverse("home"))
