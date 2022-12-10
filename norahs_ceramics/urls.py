from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path
from django.views.generic.base import TemplateView

from norahs_ceramics.sitemaps import Product_Sitemap, Static_Sitemap

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("accounts/", include("allauth.urls")),
    path("about/", include("about.urls")),
    path("products/", include("product.urls")),
    path("basket/", include("basket.urls")),
    path("customers/", include("customer.urls")),
    path("checkout/", include("checkout.urls")),
    path("contact/", include("contact.urls")),
    path("policies/", include("policies.urls")),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="robots.txt", content_type="text/plain"
        ),
    ),
    path(
        "sitemap.xml",
        sitemap,
        {
            "sitemaps": {"product": Product_Sitemap, "static": Static_Sitemap},
        },
        name="django.contrib.sitemaps.views.sitemap",
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
