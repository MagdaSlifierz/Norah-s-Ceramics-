from django.views.generic import TemplateView


class TermsAndConditionsView(TemplateView):
    """Render terms and conditions page"""

    template_name = "policies/terms.html"


class PrivacyPolicyView(TemplateView):
    """Render terms and conditions page"""

    template_name = "policies/privacy_policy.html"


class ReturnsPolicyView(TemplateView):
    """Render terms and conditions page"""

    template_name = "policies/returns.html"


class ShippingPolicyView(TemplateView):
    """Render terms and conditions page"""

    template_name = "policies/delivery.html"
