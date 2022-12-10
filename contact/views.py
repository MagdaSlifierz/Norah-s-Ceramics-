from django.conf import settings
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View

from contact.forms import ContactForm
from contact.utility import send_email


class ContactView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        """Render contact page

        Args:
            request (HttpRequest): Django request object

        Returns:
            HttpResponse: Django http response
        """
        context = {"contact_form": ContactForm()}
        return render(request, "contact/contact.html", context)

    def post(self, request: HttpRequest) -> HttpResponseRedirect:
        """Post contact form endpoint

        Args:
            request (HttpRequest): DJango request object

        Returns:
            HttpResponseRedirect: Redirect page to contact GET
        """
        contact_form = ContactForm(request.POST)
        body = render_to_string("email/body.txt")

        if contact_form.is_valid():
            success = False
            if contact_form.submit_email():
                if send_email(
                    [contact_form.cleaned_data["contact_email"]],
                    settings.EMAIL_HOST_USER,
                    body,
                    "We have got your email",
                ):
                    success = True
            if success:
                messages.success(
                    request, "Your message has been sent successfully!"
                )
            else:
                messages.error(request, "Your message couldn't be sent")
        else:
            for key, value in contact_form.errors.items():
                field_name = str(key).replace("_", " ").capitalize()
                msg = f"{field_name}: {value[0]}"
                messages.error(request, msg)
        return HttpResponseRedirect(reverse("contact"))
