from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from product.models import Product


class Product_Sitemap(Sitemap):
    changefreq = "daily"
    priority = 0.7

    def items(self):
        return Product.objects.all()

    def lastmod(self, obj):
        return obj.updated_at


class Static_Sitemap(Sitemap):

    priority = 1.0
    changefreq = "daily"

    def items(self):
        return ["about", "home"]

    def location(self, item):
        return reverse(item)
