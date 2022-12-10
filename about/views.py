from django.views.generic import TemplateView


class AboutView(TemplateView):
    """Render about page"""

    template_name = "about/about.html"
